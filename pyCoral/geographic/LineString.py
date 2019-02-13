from shapely import geometry as sg
from pyCoral import Units
from pyCoral.geographic.Point import Point # pylint: disable=import-error

class LineString:
    def __init__(self, point_list = []):
        if isinstance(point_list, list) and all(isinstance(p, Point) for p in point_list):
            self._shapely_line = sg.LineString(
                c.shapely() for c in point_list
            )
        else:
            raise TypeError('point_list must be a list of Points')

    def points(self):
         return list(map(lambda c: Point(c[0], c[1]), self._shapely_line.coords))

    def shapely(self):
        return self._shapely_line

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.points() == other.points()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
