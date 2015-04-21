import arcpy
from arcpy import env
import os
import fnmatch
env.workspace=r'F:\data\Talitha\Mapas_classificados_final\SHP\Paisagens'


LISTA2=arcpy.ListFeatureClasses()
env.workspace=r'F:\data\Talitha\Mapas_classificados_final\Raster_entrada_grass'
for i in LISTA2:
            inpu=i.replace('.shp','')
            out=inpu+'_rast.tif'
            print inpu, out
            
            arcpy.PolygonToRaster_conversion(inpu,"land_use",out,"CELL_CENTER","NONE",10)

arcpy.PolygonToRaster_conversion("classificada_19840621_24022015_utm_final","land_use",'bla',"CELL_CENTER","NONE",10).dxddx