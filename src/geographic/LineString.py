from shapely import geometry as sg

from geographic.Coordinate import Coordinate # pylint: disable=import-error

class LineString:
    def __init__(self, coordinate_list = []):
        if isinstance(coordinate_list, list) and all(isinstance(coord, Coordinate) for coord in coordinate_list):
            self._coords = coordinate_list
            self._shapely_line = sg.LineString(
                c.shapely() for c in coordinate_list
            )
        else:
            raise TypeError('coordinate_list must be a list of Coordinates')

    def coordinates(self):
        return self._coords

    def shapely(self):
        return self._shapely_line

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.coordinates() == other.coordinates()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
