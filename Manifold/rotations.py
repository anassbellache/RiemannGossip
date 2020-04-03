import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm, logm

class Rotation:
    def __init__(self, coordinates=None):
        """3 dimensional rotations Group SO(3).
        
        
        Keyword Arguments:
            coordinates {[type]} -- [description] (default: {None})
        """
        if coordinates is not None:
            self._coordinates = coordinates
        else:
            M = np.random.randn(3,3)
            self._coordinates, _ = np.linalg.qr(M)
    
    @property
    def coordinates(self):
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, matrix):
        self._coordinates = matrix
    
    def __repr__(self):
        return "SO(3) matrix: det :{}".format(np.linalg.det(self._coordinates))
    
    def distance(self, other):
        C = logm(np.matmul(self._coordinates, other._coordinates.transpose()))
        return np.linalg.norm(C)
    
    def midpoint(self, other):
        C = sqrtm(np.matmul(self._coordinates.transpose(), other._coordinates))
        C = np.matmul(self._coordinates, C)
        return Rotation(coordinates=C)