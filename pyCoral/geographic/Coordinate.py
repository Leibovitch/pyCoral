from shapely import geometry as sg

from pyCoral.Units import Units # pylint: disable=import-error

class Coordinate:
    def __init__(self, lon = 0, lat = 0):
        if lon.__class__ in [int, float]:
            lon = lon * Units.deg

        if lat.__class__ in [int, float]:
            lat = lat * Units.deg

        deg_class = Units.deg.__class__
        if isinstance(lon, deg_class) and isinstance(lat, deg_class):
            self._lon = lon
            self._lat = lat
            self._shapely_point = sg.Point([
                lon / Units.deg,
                lat / Units.deg
            ])
        else:
            raise TypeError('lon, lat must be one of [int, float, Units.deg]')

    def lon(self):
        return self._lon

    def lat(self):
        return self._lat

    def shapely(self):
        return self._shapely_point

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.lon() == other.lon() and self.lat() == other.lat()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
