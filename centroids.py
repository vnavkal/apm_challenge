"""Calculates proximities between centroids and coordinate locations

Public classes:
    ClosestCentroidCalculator

Public methods:
    furthest_nth_coordinate
"""

from numbers import Number
from typing import Iterable
import heapq
import numpy as np


def furthest_nth_proximity(centroids: np.ndarray, coordinates: Iterable, n: int) -> np.float64:
    """Max of the nth largest distance from a centroid to any coordinate"""
    proximities = _nth_proximities(coordinates, centroids, n)
    return proximities.max()


class ClosestCentroidCalculator:
    def __init__(self, centroids: np.ndarray, coordinates: Iterable) -> None:
        self._proximities = _nth_proximities(centroids, coordinates, 1)

    def num_coordinates_within(self, radius: Number) -> np.float64:
        """Number of coordinates within specified radius of any centroid"""
        return (self._proximities <= radius).sum()

    def min_radius_enveloping_percent(self, percent: Number) -> np.float64:
        """Smallest radius such that percent of coordinates are within radius of a centroid"""
        return np.percentile(self._proximities, percent, interpolation='lower')


def _nth_proximities(X: np.ndarray, Y: np.ndarray, n: int) -> np.ndarray:
    """Calculate the nth smallest distance from each element of Y to any element of X"""
    proximities = np.empty(len(Y))
    for i, y in enumerate(Y):
        proximities[i] = heapq.nsmallest(n, _distances(X, y))[-1]
    return proximities


def _distances(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    _check_dimensions(X, y)
    return np.linalg.norm(X - y, axis=1)


def _check_dimensions(X, y) -> None:
    """Check X has dimension (n, 2) and y has dimension (n,)"""
    if X.shape != (y.shape[0], 2) or len(y.shape) > 1:
        raise ValueError('X and y have incorrect dimensions {0} and {1}'.
                         format(X.shape, y.shape))
