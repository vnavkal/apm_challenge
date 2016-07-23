"""Solves the specific questions in the challenge

This executable module uses the centroids library to answer the specific
questions from the challenge.
"""

import pandas as pd
import centroids

CENTROIDS_PATH = 'centroids.csv[3][1]'
COORDINATES_PATH = 'coordinates.csv[5][1]'


def _load_centroids_from_file():
    print('Loading centroids from file...')
    array = pd.read_csv(CENTROIDS_PATH).values
    print('Finished loading centroids')
    return array


def _load_coordinates_from_file():
    print('Loading coordinates from file...')
    return pd.read_csv(COORDINATES_PATH).values
    print('Finished loading coordinates')


if __name__ == '__main__':
    centroids_ary = _load_centroids_from_file()
    coordinates_ary = _load_coordinates_from_file()
    calculator = centroids.ClosestCentroidCalculator(centroids_ary, coordinates_ary)
    print('{0} coordinates are within 5 meters of a centroid.'.
          format(calculator.num_coordinates_within(5)))
    print('{0} coordinates are within 10 meters of a centroid.'.
          format(calculator.num_coordinates_within(10)))
    print('{0} is the minimum radius R such that 80% of coordinates are within '
          'a radius R of a centroid.'.
          format(calculator.min_radius_enveloping_percent(80)))
    print('{0} is the maximum radius R such that the number of coordinates '
          'less than R meters from a centroid is at most 1000.'.
          format(centroids.furthest_nth_proximity(centroids_ary, coordinates_ary, 1001)))
