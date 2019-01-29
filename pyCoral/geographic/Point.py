from shapely import geometry as sg
import geopandas as gpd
import numpy as np

from pyCoral.Units import Units # pylint: disable=import-error

class Point:
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

    def to_mercator(self):
        p1 = gpd.GeoSeries([self.shapely()])
        p1.crs = { 'init': 'epsg:4326' }
        p1 = p1.to_crs(epsg=3395)
        return p1

    def lon(self):
        return self._lon

    def lat(self):
        return self._lat

    def shapely(self):
        return self._shapely_point
    
    def translate(self, azimuth, distance):
        c, s = np.cos(azimuth), np.sin(azimuth)
        heading = distance.to(Units.meter) * np.array([s, c])
        new_point = self.to_mercator().translate(heading[0].magnitude, heading[1].magnitude)
        new_point = new_point.to_crs(epsg=4326)
        return Point(new_point[0].x, new_point[0].y)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.lon() == other.lon() and self.lat() == other.lat()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
