import unittest
from os import path
import sys

dirpath = path.abspath(path.join(__file__, '../../../src'))
sys.path.append(dirpath)

# pylint: disable=import-error
from geographic.LineString import LineString
from geographic.Coordinate import Coordinate
# pylint: enable=import-error

class LineStringTests(unittest.TestCase):

    def test_ctor_defaultValues_initialize(self):
        l = LineString()
        self.assertEqual(l._coords, [])

    def test_ctor_badInitialValues_raiseException(self):
        self.assertRaises(TypeError, LineString, 30)
        self.assertRaises(TypeError, LineString, "")
        self.assertRaises(TypeError, LineString, {})
        self.assertRaises(TypeError, LineString, [20, 20])

    def test_equal(self):
        l1 = LineString([ Coordinate(30, 30), Coordinate(30, 31) ])
        l2 = LineString([ Coordinate(30, 30.0), Coordinate(30, 31.0) ])
        self.assertEqual(l1, l2)

    def test_non_equal(self):
        l1 = LineString([ Coordinate(30, 30), Coordinate(30, 31) ])
        l2 = LineString([ Coordinate(30, 31.0), Coordinate(30, 32.0) ])
        self.assertNotEqual(l1, l2)

if __name__ == '__main__':
    unittest.main()