import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math

lista_vects=grass.mlist_grouped ('rast', pattern='*classificada*') ['PERMANENT']
listanames=[1984,1988,1992,1996,2000,2003,2005,2009,20014]
x=0
for i in lista_vects:
    out='classificada_'+`listanames[x]`
    print i, "***",out
    grass.run_command('g.rename',rast=i+','+out)
    x=x+1
    