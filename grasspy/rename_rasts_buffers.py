import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math

lista_vects=grass.mlist_grouped ('rast', pattern='*semdissolv500rast*') ['PERMANENT']
x=0
for i in lista_vects:
    out=i.replace('semdissolv500rast','semdissolv0500rast')
    print i, "***",out
    grass.run_command('g.rename',rast=i+','+out)
    x=x+1
    