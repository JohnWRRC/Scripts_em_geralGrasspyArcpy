import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
import os
lista_meters=[1500,1000,500]
lista_vects=grass.mlist_grouped ('vect', pattern='*semdissolv*') ['PERMANENT']
cont=0
os.chdir(r'F:\data\Talitha\Mapas_classificados_final\SHP\Centroids_buffers')
for i in lista_vects:
    grass.run_command('g.region',vect=i)
    out=i.replace('semdissolv_shp','centroid')
    grass.run_command('v.extract', input=i,out='temp' ,type='centroid',overwrite=True)
    grass.run_command('v.type',input='temp',out=out,type='centroid,point')
    grass.run_command('v.out.ogr',input=out, dsn=out+'.shp',type='point')
    
    