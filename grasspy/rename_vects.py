import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math

lista_vects=grass.mlist_grouped ('vect', pattern='*semdissolv*') ['PERMANENT']

for i in lista_vects:
    out=i.replace('FINAL','2000m')
    grass.run_command('g.rename',vect=i+','+out)
    