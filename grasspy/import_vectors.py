import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch
lista_arquivos=[]
LISTA=[]
LISTA2=[]  


for file in os.listdir(r'F:\data\Talitha\Mapas_classificados_final\SHP'):
    if fnmatch.fnmatch(file, '*.shp'):
        #print file
        if "semdissolv" in file:
            #print file
            lista_arquivos.append(file)
        if "utm" in file:
            LISTA2.append(file)
del LISTA2[-1]
print LISTA2
x=0           
LISTA=lista_arquivos[0:8]
os.chdir(r'F:\data\Talitha\Mapas_classificados_final\SHP')
for i in LISTA:
    #out=i.replace('.shp','_shp')
    out2=LISTA2[x].replace('.shp',"_shp")
    #grass.run_command('v.in.ogr',dsn=i,out=out,overwrite=True)
    grass.run_command('v.in.ogr',dsn=LISTA2[x],out=out2,overwrite=True)
    grass.run_command('g.region',vect=out2,res=10)
    #grass.run_command('v.to.rast',input=out,out=out+'_rast',use='attr',column='id',overwrite=True)
    grass.run_command('v.to.rast',input=out2,out=out2+'_rast',use='attr',column='land_use',overwrite=True)
    x=x+1
    
    
    