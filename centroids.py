"""Calculates proximities between centroids and coordinate locations

Public classes:
    ClosestCentroidCalculator

Public methods:
    furthest_nth_coordinate
"""

import heapq
import numpy as np


def furthest_nth_proximity(centroids, coordinates, n):
    """Max of the nth largest distance from a centroid to any coordinate

    Parameters
    ----------
    centroids : ndarray, of shape (_,2)
        Specification of the locations of centroids
    coordinates : ndarray, of shape (_,2)
        Specification of the locations of coordinates
    n : int
        Rank of the proximity

    Returns
    -------
    np.float64
        Maximum among the set of nth largest distances between a centroid and
        the set of coordinates
    """
    proximities = _nth_proximities(coordinates, centroids, n)
    return proximities.max()


class ClosestCentroidCalculator:
    """Contains methods calculated using the closest centroid to each coordinate

    This class internally calculates and stores an array containing the distance
    from each coordinate to the closest centroid.

    Parameters
    ----------
    centroids : ndarray, of shape (_,2)
        Specification of the locations of centroids
    coordinates : ndarray, of shape (_,2)
        Specification of the locations of coordinates
    """

    def __init__(self, centroids, coordinates):
        self._proximities = _nth_proximities(centroids, coordinates, 1)

    def num_coordinates_within(self, radius):
        """Number of coordinates within specified radius of any centroid

        Parameters
        ----------
        radius : numeric
            Coordinates closer than this value to a centroid are counted

        Returns
        -------
        np.float64
        """
        return (self._proximities <= radius).sum()

    def min_radius_enveloping_percent(self, percent):
        """Smallest radius containing specified percent of coordinates

        Calculate the smallest radius such that the specified percent of
            coordinates are within that radius of a centroid

        Parameters
        ----------
        percent : numeric

        Returns
        -------
        np.float64
            Smallest radius containing percent of coordinates
        """
        return np.percentile(self._proximities, percent, interpolation='lower')


def _nth_proximities(X, Y, n):
    """nth smallest distance from each element of Y to any element of X

    Calculate, for each coordinate y in Y, the nth smallest among the set of
    distances from y to a coordinate in X.  This method is used as a helper
    method for both the ClosestCentroidCalculator methods (in which X is the set
    of centroids and Y is the set of coordinates), and the
    furthest_nth_proximity method (in which X is the set of coordinates and Y is
    the set of centroids).

    Parameters
    ----------
    X : ndarray, of shape (_,2)
    Y : ndarray, of shape (_,2)

    Returns
    -------
    np.float64
    """
    proximities = np.empty(len(Y))
    for i, y in enumerate(Y):
        proximities[i] = heapq.nsmallest(n, _distances(X, y))[-1]
    return proximities


def _distances(X, y):
    """Calculate the distances from each element of X to y"""
    _check_dimensions(X, y)
    return np.linalg.norm(X - y, axis=1)


def _check_dimensions(X, y):
    """Check X has dimension (n, 2) and y has dimension (2,)"""
    if len(X.shape) != 2:
        raise ValueError('X was {0}-dimensional, should be 2-dimensional'.
                         format(len(X.shape)))
    if X.shape[1] != 2:
        raise ValueError('X had width {0}, expected width 2'.
                         format(X.shape[1]))
    if y.shape != (2,):
        raise ValueError('y has shape {0}, expected (2,)'.
                         format(y.shape))
