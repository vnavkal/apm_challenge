import unittest
import numpy as np
from centroids import distances_from_centroid

class TestCentroids(unittest.TestCase):
    def test_distances_from_centroids(self):
        centroid = np.array((3, 4))
        coordinates_collection = np.array(((3, 4),
                                           (0, 0)))
        distances = distances_from_centroid(centroid, coordinates_collection)
        print('distances are {0}'.format(distances))
        self.assertAlmostEqual(distances[0], 0)
        self.assertAlmostEqual(distances[1], 5)

if __name__ == '__main__':
    unittest.main()
