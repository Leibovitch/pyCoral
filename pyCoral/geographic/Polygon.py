from shapely import geometry as sg
from area import area
from pyCoral.geographic.Point import Point # pylint: disable=import-error
import numpy as np
from pyCoral import Units
import geopandas as gpd

from pyCoral.geographic.Coordinate import Coordinate # pylint: disable=import-error

class Polygon:
    def __init__(self, Point_list = []):
        if isinstance(Point_list, list) and all(isinstance(point, Point) for point in Point_list):
            self._shapely_polygon = sg.Polygon(
                c.shapely() for c in Point_list
            )

            self._geopandas = gpd.GeoSeries(self._shapely_polygon)
            self._geopandas.crs = {'init': 'epsg:4326'}

        else:
            raise TypeError('Point_list must be a list of Points')

    def points(self):
        return map(lambda c: Point(c[0], c[1]), self._shapely_line.coords())

    def shapely(self):
        return self._shapely_line

    def geopandas(self):
        return self._geopandas

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.points() == other.points()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def area(self):
        geojson = {
            'type': 'MultiPoint',
            'Points': self.points()
        }
        return area(geojson) * Units.sqm
    
    def centroid(self):
        centroid = self._geopandas.to_crs(({'init': 'epsg:3857'})).centroid
        return Point.from_shapely(centroid[0].coords[0])

    def convex_hall(self):
        pass

    def boundry_length(self):
        pass
