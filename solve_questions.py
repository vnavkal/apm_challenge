"""Solves the specific questions in the challenge

This executable module uses the centroids library to answer the specific
questions from the challenge.
"""

import argparse
import numpy as np
import pandas as pd
from proximity_calculation import (
    ClosestCentroidCalculator, smallest_nth_proximity
)


def _load_centroids_from_file(path):
    print('Loading centroids from file...')
    array = pd.read_csv(path, dtype=np.float64).values
    print('Finished loading centroids')
    return array


def _load_coordinates_from_file(path):
    print('Loading coordinates from file...')
    array = pd.read_csv(path, dtype=np.float64).values
    print('Finished loading coordinates')
    return array


def _get_closest_centroid_calculator(centroids, coordinates):
    print('Initializing ClosestCentroidCalculator...')
    return ClosestCentroidCalculator(centroids, coordinates)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Calculate properties of distances between centroids and '
                    'coordinates'
    )
    parser.add_argument('centroids_path', type=str,
                        help='path to centroids file')
    parser.add_argument('coordinates_path', type=str,
                        help='path to coordinates file')
    args = parser.parse_args()

    centroids = _load_centroids_from_file(args.centroids_path)
    coordinates = _load_coordinates_from_file(args.coordinates_path)
    calculator = _get_closest_centroid_calculator(centroids, coordinates)
    print('{0} coordinates are within 5 meters of a centroid.'.
          format(calculator.num_coordinates_within(5)))
    print('{0} coordinates are within 10 meters of a centroid.'.
          format(calculator.num_coordinates_within(10)))
    print('{0} is the minimum radius R such that 80% of coordinates are within '
          'a radius R of a centroid.'.
          format(calculator.min_radius_enveloping_percent(80)))
    print('{0} is the maximum radius R such that the number of coordinates '
          'less than R meters from every centroid is at most 1000.'.
          format(smallest_nth_proximity(centroids, coordinates, 1001)))
