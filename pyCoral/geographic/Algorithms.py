import geopandas as gpd

# pylint: disable=import-error
from pyCoral.Units import Units
# pylint: enable=import-error

def distance(geometry1, geometry2):
    gs1 = gpd.GeoSeries([geometry1.shapely()])
    gs1.crs = { 'init': 'epsg:4326' }
    gs1 = gs1.to_crs(epsg=3395)

    gs2 = gpd.GeoSeries([geometry2.shapely()])
    gs2.crs = { 'init': 'epsg:4326' }
    gs2 = gs2.to_crs(epsg=3395)

    return gs1.distance(gs2)[0] * Units.m