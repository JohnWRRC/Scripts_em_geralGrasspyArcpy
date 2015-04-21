import arcpy
from arcpy import env
env.workspace=r'C:\_data\talitha\Mapas_classificados_final\SHP\Buffers'
fc=arcpy.ListFeatureClasses()

env.workspace=r'C:\_data\talitha\Mapas_classificados_final\SHP\temp'
escala=[1500,1000,500]
for i in fc:
    inp=i.replace('.shp','')
    arcpy.FeatureToPoint_management(inp,inp+'_centroid')
    for a in escala:     
        arcpy.Buffer_analysis(inp+'_centroid',inp+`a`,a,'FULL','ROUND','NONE')
        arcpy.PolygonToRaster_conversion(inp+`a`,'id',inp+`a`+'rast.img','CELL_CENTER','NONE',10)
        

