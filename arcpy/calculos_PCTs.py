import arcpy
from arcpy import env
import os




env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffers"
fcList = arcpy.ListFeatureClasses ()
env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso"

for i in fcList:
    out1=i.replace(".shp","")
    out2=out1+"_clip_Uso"
    print out
    arcpy.Clip_analysis("gradeApoio_1000m_veg_2014_12_d20_p1p2_clip_1500_v02",out1,out2)
    
env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso"   
fcList = arcpy.ListFeatureClasses ()

for fc in fcList:
    #print fc
    arcpy.AddField_management(fc,"PCT","DOUBLE", 20, 20)
    summed_total =0   
    with arcpy.da.SearchCursor(fc, "area_HA") as cursor:
        for row in cursor:
            summed_total = summed_total + row[0]
            
            expressao='!area_HA!/'+`summed_total`+'*100'
        print summed_total
        arcpy.CalculateField_management(fc,"PCT",expressao,"PYTHON")
            
    
    
   
env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffers"
fcList1 = arcpy.ListFeatureClasses ()   

env.workspace = r"F:\data\john_pc2\Marinana\Analises\buffer_clip_uso"   
fcList2 = arcpy.ListFeatureClasses ()       
x=0
for i in fcList1:
    
    print fcList1[x],"---",fcList2[x]
    i1=fcList1[x].replace(".shp","")
    i2=fcList2[x].replace(".shp","")
    out=i2+"_union"
    inp=i1+" #;"+i2+" #"
    #arcpy.Union_analysis("buffer_0100_clip_Uso #;buffer_100 #", union_teste_shp, "ALL", "", "GAPS")
    arcpy.Union_analysis(inp, out, "ALL", "", "GAPS")
    x=x+1