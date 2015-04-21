import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch
lista_arquivos=[]
LISTA=[]
LISTA=[]  


for file in os.listdir(r'F:\data\Talitha\Mapas_classificados_final\Raster_entrada_grass'):
    if fnmatch.fnmatch(file, '*.tif'):
        #print file
        LISTA.append(file)
        
          

os.chdir(r'F:\data\Talitha\Mapas_classificados_final\Raster_entrada_grass')
for i in LISTA:
    out=i.replace('.tif',"_tif")
    grass.run_command('r.in.gdal',input=i,out=out,overwrite=True)
    
    
    