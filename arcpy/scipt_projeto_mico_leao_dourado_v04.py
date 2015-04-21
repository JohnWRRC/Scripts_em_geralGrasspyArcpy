import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch
LISTA=['D04','D05','D06','E04','E05','E06','F04','F05','F06','G05','H04','H05','I04','I05']
LISTA2=['D05','E05','E06','F05','F06','H05','IO4']
LISTA3=['E06','F06','IO4']
LISTA3=['C05']


os.chdir(r'F:\data\john_pc2\mico_leao\mico-leao\saidas')
for i in LISTA3:
    query="Grid=\'"+i+"\'" 
    x=grass.read_command('v.db.select', flags='c', map='area_classificacao_2012_grid0125b_shp', column='Nome', where=query,verbose=False) 
    grass.run_command('v.extract', input='area_classificacao_2012_grid0125b_shp', output='temp', where=query, type='area', new=1,overwrite=True,verbose=False) 
    grass.run_command('v.to.rast', input='temp', out='temp_rast_masc', use="cat",overwrite=True,verbose=False) 
  
    #print x 
    
    a=re.split(',',x)
    
    
    
    cont=0 
    #print a
    letras=['A','B','C'] 
    for k in a:
        k=str(k).replace("\n",".tif") 
        #print k
        lista_arquivos=[]
        for root, dirs, files in os.walk("F:/data/john_pc2/mico_leao/mico-leao/selecao_RapidEye_tiff/selecao_RapidEye_tiff"):
            for file in files:
                if file.endswith(k):
                    print os.path.join(root, file)
                    lista_arquivos.append(os.path.join(root, file)) 
        if (len(lista_arquivos)>1):
            print "MENSAGEM FORAM ENCONTRADOS :",lista_arquivos, "UTILIZANDO O PRIMEIRO" 
            
        j=i 
        if len(a)>1:
            j=i+"_"+letras[cont] 
            cont=cont+1 
        #print j
        #print lista_arquivos
        grass.run_command ('r.in.gdal', flags='o' ,input=lista_arquivos[0], output=j ,overwrite=True, verbose = False) 
        grass.run_command('g.region', rast=j+'.1',verbose=False) 
        grass.run_command('v.to.rast', input='amostras_apa_sao_joao_shp', out='amostras_raster', use='attr', column='COD', overwrite=True)
        grass.run_command('r.mask', input='temp_rast_masc', flags='o', verbose=False,overwrite=True ) 
        grass.run_command('i.group', group=j ,subgroup=j,  input=j+'.1' ',' +j+'.2' ',' +j+'.3',verbose=False,overwrite=True) 
        grass.run_command('i.gensigset', trainingmap='amostras_raster', group=j, subgroup=j, signaturefile=j+'_sigfile_to_smap',overwrite=True,verbose=False) 
        grass.run_command('g.region', rast=j+'.1',verbose=False) 
        grass.run_command('i.smap', group=j, subgroup=j, signaturefile=j+'_sigfile_to_smap', output=j+'_classificacao_smap', blocksize=2048,verbose=False,overwrite=True) 
        grass.run_command('r.neighbors', input=j+'_classificacao_smap', out=j+'_classificacao_smap_limpo_05', method='mode', size=05,verbose=False,overwrite=True) 
        grass.run_command('r.to.vect', input=j+'_classificacao_smap_limpo_05', out=j+'_classificacao_smap_limpo_05_vect', feature='area',verbose=False,overwrite=True ) 
        grass.run_command('r.out.gdal', input=j+'_classificacao_smap_limpo_05', out=j+'_classificacao_smap_limpo_05_tif.tif', format='GTiff',verbose=False,overwrite=True)
        grass.run_command('v.out.ogr', input=j+'_classificacao_smap_limpo_05_vect', dsn=j+'_classificacao_smap_limpo_05_vect.shp', type='area',verbose=False,overwrite=True)
        grass.run_command('r.mask', flags='r',verbose=False) 
        grass.run_command('g.remove',flags='f', vect='temp',verbose=False) 
        grass.run_command('g.remove',flags='f', rast='temp_rast_masc',verbose=False) 
        grass.run_command('g.remove',flags='f', rast='amostras_raster',verbose=False) 
        grass.run_command('g.remove',flags='f', rast='amostras_raster',verbose=False) 
        
      