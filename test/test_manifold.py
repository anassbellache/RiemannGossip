import unittest
from Manifold.posn import SymPos
from Manifold.rotations import Rotation


class TestSymMatrix(unittest.TestCase):
    
    def test_distance(self):
        posdn1 = SymPos(3)
        posdn2 = SymPos(3)
        posdn3 = SymPos(3)

        trangular_distance = posdn1.distance(posdn2) + posdn2.distance(posdn3)

        self.assertAlmostEqual(posdn1.distance(posdn1), 0)
        self.assertGreater(posdn1.distance(posdn2), 0)
        self.assertGreaterEqual(trangular_distance, posdn1.distance(posdn3))
    
    def test_midpoint(self):
        posdn1 = SymPos(3)
        posdn2 = SymPos(3)

        mid = posdn1.midpoint(posdn2)
        dist1 = posdn1.distance(posdn2)
        dist2 = posdn1.distance(mid) + posdn2.distance(mid)
        dist3 = 2*posdn1.distance(mid)
        dist4 = 2*posdn2.distance(mid)

        self.assertAlmostEqual(dist1, dist2)
        self.assertAlmostEqual(dist1, dist3)
        self.assertAlmostEqual(dist3, dist4)
    
class TestRotations(unittest.TestCase):

    def test_distance(self):
        rotation1 = Rotation()
        rotation2 = Rotation()
        rotation3 = Rotation()

        trangular_distance = rotation1.distance(rotation2) + rotation2.distance(rotation3)

        self.assertAlmostEqual(rotation1.distance(rotation1), 0)
        self.assertGreater(rotation1.distance(rotation2), 0)
        self.assertGreaterEqual(trangular_distance, rotation1.distance(rotation3))
    
    def test_midpoint(self):
        rotation1 = Rotation()
        rotation2 = Rotation()

        mid = rotation1.midpoint(rotation2)
        dist1 = rotation1.distance(rotation2)
        dist2 = rotation1.distance(mid) + rotation2.distance(mid)
        dist3 = 2*rotation1.distance(mid)
        dist4 = 2*rotation2.distance(mid)

        self.assertAlmostEqual(dist1, dist2)
        self.assertAlmostEqual(dist1, dist3)
        self.assertAlmostEqual(dist1, dist4)



if __name__ == '__main__':
    unittest.main()