import unittest
from os import path
import sys

dirpath = path.abspath(path.join(__file__, '../../../src'))
sys.path.append(dirpath)

# pylint: disable=import-error
from Units import Units
from geographic.LineString import LineString
from geographic.Coordinate import Coordinate
from geographic import Algorithms
# pylint: enable=import-error

class AlgorithmsTests(unittest.TestCase):

    def test_distance_linestring2coordinate_nonzero(self):
        line = LineString([ Coordinate(30, 30), Coordinate(32, 32) ])
        coordinate = Coordinate(31, 31)
        d = Algorithms.distance(line, coordinate)
        self.assertEqual(d, 446.6629994992208 * Units.meter)

    def test_distance_linestring2coordinate_oneDegree(self):
        line = LineString([ Coordinate(30, 0.001), Coordinate(30, -0.001) ])
        coordinate = Coordinate(31, 0)
        d = Algorithms.distance(coordinate, line)
        self.assertEqual(d, 111319.49079327332 * Units.meter)

if __name__ == '__main__':
    unittest.main()