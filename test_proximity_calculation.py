import unittest
import numpy as np
from proximity_calculation import (
    ClosestCentroidCalculator, smallest_nth_proximity
)


class TestSmallestNthProximity(unittest.TestCase):
    def setUp(self):
        self._centroids = np.array(((0, 0),
                                   (1, 0)))
        self._coordinates = np.array(((1, 1),
                                      (4, 4),
                                      (-6, -8)))

    def test_first_proximity(self):
        self.assertAlmostEqual(
            smallest_nth_proximity(self._centroids, self._coordinates, 1),
            1
        )

    def test_second_proximity(self):
        self.assertAlmostEqual(
            smallest_nth_proximity(self._centroids, self._coordinates, 2),
            5
        )

    def test_third_proximity(self):
        self.assertAlmostEqual(
            smallest_nth_proximity(self._centroids, self._coordinates, 3),
            10
        )


class TestClosestCentroidCalculator(unittest.TestCase):
    def setUp(self):
        centroids = np.array(((0, 0),
                              (1, 0)))
        coordinates = np.array(((1, 1),
                                (4, 4)))
        self._calculator = ClosestCentroidCalculator(centroids, coordinates)

    def test_num_coordinates_within_0(self):
        self.assertEqual(self._calculator.num_coordinates_within(0), 0)

    def test_num_coordinates_within_1(self):
        self.assertEqual(self._calculator.num_coordinates_within(1), 1)

    def test_num_coordinates_within_5(self):
        self.assertEqual(self._calculator.num_coordinates_within(5), 2)

    def test_num_coordinates_within_6(self):
        self.assertEqual(self._calculator.num_coordinates_within(6), 2)

    def test_min_radius_enveloping_10_percent(self):
        self.assertAlmostEqual(
            self._calculator.min_radius_enveloping_percent(10),
            1
        )

    def test_min_radius_enveloping_50_percent(self):
        self.assertAlmostEqual(
            self._calculator.min_radius_enveloping_percent(50),
            1
        )
    def test_min_radius_enveloping_60_percent(self):
        self.assertAlmostEqual(
            self._calculator.min_radius_enveloping_percent(60),
            5
        )
    def test_min_radius_enveloping_100_percent(self):
        self.assertAlmostEqual(
            self._calculator.min_radius_enveloping_percent(100),
            5
        )


if __name__ == '__main__':
    unittest.main()
