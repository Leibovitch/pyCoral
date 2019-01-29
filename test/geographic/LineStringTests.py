import unittest
from os import path
import sys

dirpath = path.abspath(path.join(__file__, '../../..'))
sys.path.append(dirpath)

from pyCoral.geographic.LineString import LineString
from pyCoral.geographic.Point import Point

class LineStringTests(unittest.TestCase):

    def test_ctor_defaultValues_initialize(self):
        l = LineString()
        self.assertEqual(l.points(), [])

    def test_ctor_badInitialValues_raiseException(self):
        self.assertRaises(TypeError, LineString, 30)
        self.assertRaises(TypeError, LineString, "")
        self.assertRaises(TypeError, LineString, {})
        self.assertRaises(TypeError, LineString, [20, 20])

    def test_equal(self):
        l1 = LineString([ Point(30, 30), Point(30, 31) ])
        l2 = LineString([ Point(30, 30.0), Point(30, 31.0) ])
        self.assertEqual(l1, l2)

    def test_non_equal(self):
        l1 = LineString([ Point(30, 30), Point(30, 31) ])
        l2 = LineString([ Point(30, 31.0), Point(30, 32.0) ])
        self.assertNotEqual(l1, l2)

    def test_Points(self):
        points = [ Point(30, 30), Point(30, 31) ]
        l1 = LineString(points)

        self.assertEqual(l1.points(), points)

if __name__ == '__main__':
    unittest.main()