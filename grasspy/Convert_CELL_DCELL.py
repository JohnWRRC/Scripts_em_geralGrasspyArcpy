import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch


ListMapsGroupCalc=grass.mlist_grouped ('rast', pattern='*FLT_bin*') ['PERMANENT']
for i in ListMapsGroupCalc:
    #print i
    expressao=i+'_float='+i+'*1.0'
    grass.mapcalc(expressao, overwrite = True, quiet = True)