import numpy as np
from sklearn.datasets import make_spd_matrix
from scipy.linalg import sqrtm, logm, expm
import matplotlib.pyplot as plt

class SymPos:
    
    def __init__(self, dimension, matrix=None):
        """Riemannian Manifold of SO(n) the space of geometry
        
        Arguments:
            dimension {int} -- dimension of the underlying Euclidean space the rotation acts on
        
        Keyword Arguments:
            matrix {np.ndarray} -- matrix represenation of the rotation (default: {None})
        """
        self._dim = dimension
        if matrix is not None:
            self._coordinates = matrix
        else:
            self._coordinates = make_spd_matrix(dimension)
        
    @property
    def coordinates(self):
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, matrix):
        self._coordinates = matrix
    
    def __repr__(self):
        return "Pos({}) matrix: det :{}".format(self._dim, np.linalg.det(self._coordinates))
    
    def __hash__(self):
        return hash(str(self._coordinates))
    
    def distance(self, other):
        """Defines a distance function between two positive definite matrices
        
        Arguments:
            other {SymPos} -- The positive definite matrix to calculate the distance
        
        Returns:
            float -- the distance (a positive number)
        """
        C = np.matmul(self._coordinates, np.linalg.inv(other._coordinates))
        return np.linalg.norm(logm(C))
    
    def midpoint(self, other):
        """Calculates the midpoint between two positive definite matrices
        
        Arguments:
            other {SymPos} -- A positive definite matrix 
        
        Returns:
            SymPos -- The midpoint of the current and other matrices
        """
        M, N = self._coordinates, other._coordinates
        res = np.matmul(np.linalg.inv(sqrtm(M)), N)
        res = sqrtm(np.matmul(res, np.linalg.inv(sqrtm(M))))
        res = np.matmul(sqrtm(M), res)
        res = np.matmul(res, sqrtm(M))
        return SymPos(self._dim, matrix=res)
        
