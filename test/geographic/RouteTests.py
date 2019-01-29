from datetime import datetime, timedelta

import unittest

# pylint: disable=import-error
from pyCoral.geographic import Point, Route
# pylint: enable=import-error

class RouteTests(unittest.TestCase):

    def input(self):
        return [{
            'time': datetime.strptime('1/1/2018', '%d/%m/%Y'),
            'location': Point(0, 0)
        },{
            'time': datetime.strptime('2/1/2018', '%d/%m/%Y'),
            'location': Point(0, 1)
        },{
            'time': datetime.strptime('3/1/2018', '%d/%m/%Y'),
            'location': Point(0, 2)
        }]

    def test_ctor_defaultValues_initializeEmptyList(self):
        r = Route()
        self.assertEqual(r._vec4_list, [])

    def test_ctor_initializeList(self):
        input = self.input()
        r = Route(input)
        self.assertEqual(r._vec4_list, input)

    def test_ctor_badInitialValues_raiseException(self):
        self.assertRaises(TypeError, Route, 30)
        self.assertRaises(TypeError, Route, "")
        self.assertRaises(TypeError, Route, {})
        self.assertRaises(TypeError, Route, [20, 20])

    def test_equal(self):
        input = self.input()
        r1 = Route(input)
        r2 = Route(input)
        self.assertEqual(r1, r2)

    def test_non_equal(self):
        input = self.input()
        r1 = Route(input)
        r2 = Route([])
        self.assertNotEqual(r1, r2)

    def test_interpolate_onExistingPoint(self):
        input = self.input()
        r1 = Route(input)

        result = r1.interpolate(input[1]['time'])
        self.assertIsInstance(result, Point)
        self.assertEqual(result, Point(0, 1))

    def test_interpolate_midPoint(self):
        input = self.input()
        r1 = Route(input)

        result = r1.interpolate(input[0]['time'] + timedelta(hours=12))
        self.assertIsInstance(result, Point)
        self.assertEqual(result, Point(0, 0.5))


if __name__ == '__main__':
    unittest.main()