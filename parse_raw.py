import sys

import fiona
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
import shapely.geometry 

fn=sys.argv[1]

with fiona.open(fn) as uk_gis:
    #print header
    print("objectid,name,area,centroid_x, centroid_y")
    for shape in uk_gis:
        #objectid = shape["objectid"]
        properties = shape["properties"]
        objectid = properties["objectid"]
        area_name = properties["lad17nm"]
        geom = shape["geometry"]

        if geom["type"] == 'MultiPolygon':
            mp = MultiPolygon(shapely.geometry.shape(geom))
            areas = []
            for p in list(mp):
                areas.append(p.area)
            max_area = max(areas)
            max_polygon = list(mp)[areas.index(max_area)]

            areas.remove(max_area)
           
            for a in areas:
                if a >= max_area/50:
                    sys.stderr.write("Warning multi-polygon for objectid " \
                        + str(objectid) + "\n")

            centroid = max_polygon.centroid
            print(str(objectid) + "," + str(area_name) + "," + \
                    str(max_polygon.area) + "," + \
                    str(centroid.x) + "," + str(centroid.y)) 

        elif geom["type"] == 'Polygon':
            p = Polygon(shapely.geometry.shape(geom))

            centroid = p.centroid
            print(str(objectid) + "," + str(area_name) + "," + \
                    str(p.area) + "," + \
                    str(centroid.x) + "," + str(centroid.y))
