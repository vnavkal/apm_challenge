"""Calculates proximities between centroids and coordinate locations"""

import numpy as np
from numbers import Number
import heapq

def distances(X: np.ndarray, y: np.ndarray):
    _check_dimensions(X, y)
    return np.linalg.norm(X - y, axis=1)


def within_distance(X, y, distance):
    first_small_enough_distance = next(x for x in distances(X, y) if x <= distance)
    return (first_small_enough_distance is not None)


def _check_dimensions(X, y):
    """Check X has dimension (n, 2) and y has dimension (n,)"""
    if X.shape != (y.shape[0], 2) or len(y.shape) > 1:
        raise ValueError('X and y have incorrect dimensions {0} and {1}'.
                         format(X.shape, y.shape))

class ClosestCentroidCalculator:
    def __init__(self, centroids: np.ndarray, coordinates: np.ndarray):
        self._calculate_closest_centroids(self, centroids, coordinates)

    def num_coordinates_within(self, radius: Number):
        return (self._proximities <= radius).sum()

    def min_radius_enveloping_percent(self, percent: Number):
        return (np.percentile(self._proximities, percent, interpolation='lower'))

    def _calculate_closest_centroids(self, centroids: np.ndarray, coordinates: np.ndarray):
        proximities = np.empty(len(coordinates))
        for i, coordinate_pair in enumerate(coordinates):
            proximities[i] = 
        self._proximities = np.array([
            distances(centroids, coordinate_pair) for coordinate_pair in coordinates
        ])

class DistanceCalculator:
    def __init__(self, X: np.ndarray, Y: np.ndarray, n: int):
        self._calculate_nth_proximities(X, Y, n)

    def _calculate_nth_proximities(X, Y, n):
        self._proximities = np.empty(len(X))
        for i, y in enumerate(Y):
            self._proximities[i] = heapq.nsmallest(n, distances(X, y))[-1]
