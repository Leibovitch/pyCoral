import unittest
from os import path
import sys

dirpath = path.abspath(path.join(__file__, '../../../src'))
sys.path.append(dirpath)

# pylint: disable=import-error
from geographic.Coordinate import Coordinate
from Units import Units
# pylint: enable=import-error

class CoordinateTests(unittest.TestCase):

    def test_ctor_defaultValues_initialize(self):
        c = Coordinate()
        self.assertEqual(c.lon(), 0 * Units.deg)
        self.assertEqual(c.lat(), 0 * Units.deg)

    def test_ctor_initialValues_initialize(self):
        c = Coordinate(30, 30 * Units.deg)
        self.assertEqual(c.lon(), 30 * Units.deg)
        self.assertEqual(c.lat(), 30 * Units.deg)

    def test_ctor_badInitialValues_raiseException(self):
        self.assertRaises(TypeError, Coordinate, 30, "Four")

    def test_equal(self):
        c1 = Coordinate(30, 30)
        c2 = Coordinate(30, 30.0)
        self.assertEqual(c1, c2)

    def test_non_equal(self):
        c1 = Coordinate(30, 30)
        c2 = Coordinate(30, 31)
        self.assertNotEqual(c1, c2)

if __name__ == '__main__':
    unittest.main()