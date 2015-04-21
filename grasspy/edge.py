#avancada (13)nas paisagens dentro de buffers de 500, 1000, 1500 e 2000 metros.
 #!/c/Python25 python
 #import sys, os, numpy #sys, os, PIL, numpy, Image, ImageEnhance
import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects
import os

expressao5='bintem_dila_edge_int=int(bintem_dila_edge)'
grass.mapcalc(expressao5, overwrite = True, quiet = True)  

grass.run_command('g.region',rast='bintem_dila_edge_int')
x=grass.read_command('r.stats',flags='a',input='bintem_dila_edge_int')
print x

y=x.split('\n')
os.chdir(dirs)
txtreclass=open(txtname,'w')
txtreclass.write('COD'',''HA\n')
print y
#if y!=0:

  #for i in y:
    #if i !='':
      ###print i
      #f=i.split(' ')
      #if '*' in f :
        #break
      #else:
        ###print f
        #ids=f[0]
        #ids=int(ids)
        ###print ids
        #ha=f[1]
        #ha=float(ha)
        #haint=int(ha)
        #haint=haint/10000+1
        ###print haint
        
        ###print haint
        
        #txtreclass.write(`ids`+','+`haint`+'\n')
  
  #txtreclass.close()

        
        
        