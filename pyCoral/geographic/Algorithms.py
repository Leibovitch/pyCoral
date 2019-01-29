import geopandas as gpd
import numpy as np
from pyCoral import Units
from pyCoral.geographic import Point


def distance(geometry1, geometry2):
    gs1 = gpd.GeoSeries([geometry1.shapely()])
    gs1.crs = { 'init': 'epsg:4326' }
    gs1 = gs1.to_crs(epsg=3395)

    gs2 = gpd.GeoSeries([geometry2.shapely()])
    gs2.crs = { 'init': 'epsg:4326' }
    gs2 = gs2.to_crs(epsg=3395)

    return gs1.distance(gs2)[0] * Units.m

def azimuth(point1, point2):
    # check input
    p1 = gpd.GeoSeries([point1.shapely()])
    p1.crs = { 'init': 'epsg:4326' }
    p1 = p1.to_crs(epsg=3395)

    p2 = gpd.GeoSeries([point2.shapely()])
    p2.crs = { 'init': 'epsg:4326' }
    p2 = p2.to_crs(epsg=3395)

    delta_y = p2.y - p1.y
    delta_x = p2.x - p1.x
    norm = np.sqrt(delta_y ** 2 + delta_x ** 2)

    if delta_x[0] < 0:
        factor = -1
    else:
        factor = 1 

    return (((np.arccos( delta_y /norm )[0] * factor) * Units.radian)).to(Units.degree)