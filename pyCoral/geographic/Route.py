from datetime import datetime

from pyCoral.Units import Units, fromTimedelta
from pyCoral.geographic import Coordinate, Algorithms

class Route:
    def __init__(self, vec4_list=[]):
        if isinstance(vec4_list, list) and all(map(lambda vec4: self.validate_vec4(vec4), vec4_list)):
            self._vec4_list = vec4_list

            if len(vec4_list) > 0:
                self._start_time = vec4_list[0]['time']
                self._end_time = vec4_list[len(vec4_list) - 1]['time']
            else:
                self._start_time = self._end_time = datetime(2000, 1, 1)
        else:
            raise TypeError('vec4_list must be a list of dict containing time and location')

    def validate_vec4(self, vec4):
        return isinstance(vec4['time'], datetime) and isinstance(vec4['location'], Coordinate)

    def interpolate(self, time):
        if not (self._start_time < time <= self._end_time):
            raise RuntimeError("Interpolation time must be within route range")

        i = 0
        while self._vec4_list[i]['time'] < time:
            i += 1

        v1, v2 = self._vec4_list[i-1], self._vec4_list[i]

        distance = Algorithms.distance(v1['location'], v2['location'])
        velocity = distance / fromTimedelta(v2['time'] - v1['time'])
        azimuth = Algorithms.azimuth(v1['location'], v2['location'])

        result = Coordinate.move(v1, azimuth, velocity * fromTimedelta(time - v1['time']))

        return result

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._vec4_list == other._vec4_list
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
