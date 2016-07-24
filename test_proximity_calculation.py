import unittest
import numpy as np
from proximity_calculation import ClosestCentroidCalculator, smallest_nth_proximity


class TestFurthestNthCoordinate(unittest.TestCase):
    def test_furthest_nth_coordinate(self):
        centroids = np.array(((0, 0),
                              (1, 0)))
        coordinates = np.array(((1, 1),
                                (4, 4),
                                (-6, -8)))
        self.assertAlmostEqual(smallest_nth_proximity(centroids, coordinates, 1), 1)
        self.assertAlmostEqual(smallest_nth_proximity(centroids, coordinates, 2), 5)
        self.assertAlmostEqual(smallest_nth_proximity(centroids, coordinates, 3), 10)


class TestClosestCentroidCalculator(unittest.TestCase):
    def setUp(self):
        centroids = np.array(((0, 0),
                              (1, 0)))
        coordinates = np.array(((1, 1),
                                (4, 4)))
        self._calculator = ClosestCentroidCalculator(centroids, coordinates)

    def test_num_coordinates_within(self):
        self.assertEqual(self._calculator.num_coordinates_within(0), 0)
        self.assertEqual(self._calculator.num_coordinates_within(1), 1)
        self.assertEqual(self._calculator.num_coordinates_within(5), 2)
        self.assertEqual(self._calculator.num_coordinates_within(6), 2)

    def test_min_radius_enveloping_percent(self):
        self.assertAlmostEqual(self._calculator.min_radius_enveloping_percent(10), 1)
        self.assertAlmostEqual(self._calculator.min_radius_enveloping_percent(50), 1)
        self.assertAlmostEqual(self._calculator.min_radius_enveloping_percent(60), 5)
        self.assertAlmostEqual(self._calculator.min_radius_enveloping_percent(100), 5)


if __name__ == '__main__':
    unittest.main()
