import unittest
import numpy as np
from centroids import ClosestCentroidCalculator, furthest_nth_proximity


class TestFurthestNthCoordinate(unittest.TestCase):
    def test_furthest_nth_coordinate(self):
        centroids = np.array(((0, 0),
                              (1, 0)))
        coordinates = np.array(((1, 1),
                                (4, 4)))
        self.assertAlmostEqual(furthest_nth_proximity(centroids, coordinates, 1),
                               np.linalg.norm((1, 1)))
        self.assertAlmostEqual(furthest_nth_proximity(centroids, coordinates, 2),
                               np.linalg.norm((4, 4)))


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
        # self.assertIsNone(self._calculator.min_radius_enveloping_percent(10))
        self.assertAlmostEqual(self._calculator.min_radius_enveloping_percent(50), 1)
        self.assertAlmostEqual(self._calculator.min_radius_enveloping_percent(100), 5)


if __name__ == '__main__':
    unittest.main()
