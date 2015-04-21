import arcpy
from arcpy import env
import os

env.workspace = r"F:\data\john_pc2\Marinana\Geoprocessamento\Geoprocessamento_Dados_Nagy\buffers"

fcList = arcpy.ListFeatureClasses ()

env.workspace=r"F:\data\john_pc2\Marinana\Geoprocessamento\Geoprocessamento_Dados_Nagy\buffers\mean_tifs"
v23S48_SN_tif = "23S48_dleciv.tif"
v23S48_dleciv_tif = "23S48_dleciv.tif"
for i in fcList:
    out=i.replace(".shp","decliv")
    arcpy.gp.ZonalStatisticsAsTable_sa(i, "name", v23S48_dleciv_tif,out, "DATA", "ALL")
    
    
v23S48_alt = "23S48_alt.tif"
for i in fcList:
    out=i.replace(".shp","alt")
    arcpy.gp.ZonalStatisticsAsTable_sa(i, "name", v23S48_alt,out, "DATA", "ALL")    

