### clip 

import arcpy
import os
from arcpy import env
from arcpy.sa import *


arcpy.env.workspace = "F:\data\john_pc2\Marinana\Analises\buffers"

buffer_mask = "F:\\data\\john_pc2\\Marinana\\Analises\\buffers\\buffer_1000.shp"

#rasterList = arcpy.ListRasters()
fcList=arcpy.ListFeatureClasses ()

arcpy.env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso\buffer_1000_separados"

                        
buffer_1000 = "buffer_1000"
with arcpy.da.SearchCursor(buffer_1000, "name") as cursor:
        for row in cursor:
                print row
                sl=str(''.join(row))
                out="buffer_1000_sitio_"+sl
                print out
                query="\"name\" =""" '\''+sl+'\'' 
                #sl=unicode.split(row)
                arcpy.SelectLayerByAttribute_management(buffer_1000 , "NEW_SELECTION",query)
                arcpy.Clip_analysis("buffer_1000_clip_Uso_2015_01_d09","buffer_1000",out,"")
                arcpy.AddField_management(out,"area_HA","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                arcpy.AddField_management(out,"Name","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                name="\""+sl+"\""
                arcpy.CalculateField_management(out,"Name",name,"PYTHON") 
                arcpy.CalculateField_management(out,"area_HA","!shape.area@hectares!","PYTHON_9.3","#")             
                arcpy.AddField_management(out, 'PCT', "DOUBLE", 20, 20)
                


fcList=arcpy.ListFeatureClasses () 
for fc in fcList:
        summed_total=0
        with arcpy.da.SearchCursor(fc, "area_HA") as cursor:
                for row in cursor:
                        summed_total = summed_total + row[0] 
                        expressao='!area_HA!/'+`summed_total`+'*100'
                arcpy.CalculateField_management(fc,"PCT",expressao,"PYTHON")
                        
                        
                        
arcpy.env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso\buffer_0100_separados"
buffer_100 = "buffer_100"
with arcpy.da.SearchCursor(buffer_100, "name") as cursor:
        for row in cursor:
                print row
                sl=str(''.join(row))
                out="buffer_100_sitio_"+sl
                print out
                query="\"name\" =""" '\''+sl+'\'' 
                #sl=unicode.split(row)
                arcpy.SelectLayerByAttribute_management(buffer_100 , "NEW_SELECTION",query)
                arcpy.Clip_analysis("buffer_1000_clip_Uso_2015_01_d09","buffer_100",out,"")
                arcpy.AddField_management(out,"area_HA","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                arcpy.AddField_management(out,"Name","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                name="\""+sl+"\""
                arcpy.CalculateField_management(out,"Name",name,"PYTHON") 
                arcpy.CalculateField_management(out,"area_HA","!shape.area@hectares!","PYTHON_9.3","#")             
                arcpy.AddField_management(out, 'PCT', "DOUBLE", 20, 20)
                summed_total=0
                with arcpy.da.SearchCursor(out, "area_HA") as cursor:
                        for row in cursor:
                                summed_total = summed_total + row[0] 
                                expressao='!area_HA!/'+`summed_total`+'*100'
                        arcpy.CalculateField_management(out,"PCT",expressao,"PYTHON")
                        
                        
                        
                        
                                                
arcpy.env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso\buffer_0200_separados"
buffer_200 = "buffer_200"
with arcpy.da.SearchCursor(buffer_200, "name") as cursor:
        for row in cursor:
                print row
                sl=str(''.join(row))
                out="buffer_200_sitio_"+sl
                print out
                query="\"name\" =""" '\''+sl+'\'' 
                #sl=unicode.split(row)
                arcpy.SelectLayerByAttribute_management(buffer_200 , "NEW_SELECTION",query)
                arcpy.Clip_analysis("buffer_1000_clip_Uso_2015_01_d09","buffer_200",out,"")
                arcpy.AddField_management(out,"area_HA","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                arcpy.AddField_management(out,"Name","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                name="\""+sl+"\""
                arcpy.CalculateField_management(out,"Name",name,"PYTHON") 
                arcpy.CalculateField_management(out,"area_HA","!shape.area@hectares!","PYTHON_9.3","#")             
                arcpy.AddField_management(out, 'PCT', "DOUBLE", 20, 20)
                summed_total=0
                with arcpy.da.SearchCursor(out, "area_HA") as cursor:
                        for row in cursor:
                                summed_total = summed_total + row[0] 
                                expressao='!area_HA!/'+`summed_total`+'*100'
                        arcpy.CalculateField_management(out,"PCT",expressao,"PYTHON")
                        



arcpy.env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso\buffer_0250_separados"
buffer_300 = "buffer_300_v02"
with arcpy.da.SearchCursor(buffer_300, "name") as cursor:
        for row in cursor:
                print row
                sl=str(''.join(row))
                out="buffer_300_sitio_"+sl
                print out
                query="\"name\" =""" '\''+sl+'\'' 
                #sl=unicode.split(row)
                arcpy.SelectLayerByAttribute_management(buffer_300 , "NEW_SELECTION",query)
                arcpy.Clip_analysis("buffer_1000_clip_Uso_2015_01_d09","buffer_300_v02",out,"")
                arcpy.AddField_management(out,"area_HA","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                arcpy.AddField_management(out,"Name","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                name="\""+sl+"\""
                arcpy.CalculateField_management(out,"Name",name,"PYTHON") 
                arcpy.CalculateField_management(out,"area_HA","!shape.area@hectares!","PYTHON_9.3","#")             
                arcpy.AddField_management(out, 'PCT', "DOUBLE", 20, 20)
                summed_total=0
                with arcpy.da.SearchCursor(out, "area_HA") as cursor:
                        for row in cursor:
                                summed_total = summed_total + row[0] 
                                expressao='!area_HA!/'+`summed_total`+'*100'                                                                                                                                                    
                        arcpy.CalculateField_management(out,"PCT",expressao,"PYTHON")
                                                                        





arcpy.env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso\buffer_0400_separados"
buffer_500 = "buffer_500"
with arcpy.da.SearchCursor(buffer_500, "name") as cursor:
        for row in cursor:
                print row
                sl=str(''.join(row))
                out="buffer_500_sitio_"+sl
                print out
                query="\"name\" =""" '\''+sl+'\'' 
                #sl=unicode.split(row)
                arcpy.SelectLayerByAttribute_management(buffer_500 , "NEW_SELECTION",query)
                arcpy.Clip_analysis("buffer_1000_clip_Uso_2015_01_d09","buffer_500",out,"")
                arcpy.AddField_management(out,"area_HA","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                arcpy.AddField_management(out,"Name","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                name="\""+sl+"\""
                arcpy.CalculateField_management(out,"Name",name,"PYTHON") 
                arcpy.CalculateField_management(out,"area_HA","!shape.area@hectares!","PYTHON_9.3","#")             
                arcpy.AddField_management(out, 'PCT', "DOUBLE", 20, 20)
                summed_total=0
                with arcpy.da.SearchCursor(out, "area_HA") as cursor:
                        for row in cursor:
                                summed_total = summed_total + row[0] 
                                expressao='!area_HA!/'+`summed_total`+'*100'
                        arcpy.CalculateField_management(out,"PCT",expressao,"PYTHON")
                        
                                                                                                


arcpy.env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso\buffer_0400_separados"
buffer_400 = "buffer_400"
with arcpy.da.SearchCursor(buffer_400, "name") as cursor:
        for row in cursor:
                print row
                sl=str(''.join(row))
                out="buffer_400_sitio_"+sl
                print out
                query="\"name\" =""" '\''+sl+'\'' 
                #sl=unicode.split(row)
                arcpy.SelectLayerByAttribute_management(buffer_400 , "NEW_SELECTION",query)
                arcpy.Clip_analysis("buffer_1000_clip_Uso_2015_01_d09","buffer_400",out,"")
                arcpy.AddField_management(out,"area_HA","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                arcpy.AddField_management(out,"Name","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                name="\""+sl+"\""
                arcpy.CalculateField_management(out,"Name",name,"PYTHON") 
                arcpy.CalculateField_management(out,"area_HA","!shape.area@hectares!","PYTHON_9.3","#")             
                arcpy.AddField_management(out, 'PCT', "DOUBLE", 20, 20)
                summed_total=0
                with arcpy.da.SearchCursor(out, "area_HA") as cursor:
                        for row in cursor:
                                summed_total = summed_total + row[0] 
                                expressao='!area_HA!/'+`summed_total`+'*100'
                        arcpy.CalculateField_management(out,"PCT",expressao,"PYTHON")
                        
                        
arcpy.env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso\buffer_0400_separados"
buffer_500 = "buffer_500"
with arcpy.da.SearchCursor(buffer_mask, "name") as cursor:
        for row in cursor:
                print row
                sl=str(''.join(row))
                out="buffer_500_sitio_"+sl
                print out
                query="\"name\" =""" '\''+sl+'\'' 
                #sl=unicode.split(row)
                arcpy.SelectLayerByAttribute_management(buffer_500 , "NEW_SELECTION",query)
                arcpy.Clip_analysis("buffer_1000_clip_Uso_2015_01_d09","buffer_400",out,"")
                arcpy.AddField_management(out,"area_HA","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                arcpy.AddField_management(out,"Name","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                name="\""+sl+"\""
                arcpy.CalculateField_management(out,"Name",name,"PYTHON") 
                arcpy.CalculateField_management(out,"area_HA","!shape.area@hectares!","PYTHON_9.3","#")             
                arcpy.AddField_management(out, 'PCT', "DOUBLE", 20, 20)
                summed_total=0
                with arcpy.da.SearchCursor(out, "area_HA") as cursor:
                        for row in cursor:
                                summed_total = summed_total + row[0] 
                                expressao='!area_HA!/'+`summed_total`+'*100'
                        arcpy.CalculateField_management(out,"PCT",expressao,"PYTHON")