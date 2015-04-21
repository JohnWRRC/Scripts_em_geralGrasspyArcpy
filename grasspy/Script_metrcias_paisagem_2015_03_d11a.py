import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch


def createtxtED(mapa,txtname,folder,t):
  x=grass.read_command('r.stats',flags='a',input=mapa)
  y=x.split('\n')
  os.chdir(r'F:\data\Talitha\Mapas_classificados_final\saidas_grass\saidas_2015_03_d11')
  os.chdir(folder)
  txtreclass=open(txtname,'w')
  if t==7:
    txtreclass.write('CodEd_30m'',''ClasEd_30m'',''A_HaEd_30m\n')
  else:
    txtreclass.write('CodEd_90m'',''ClasEd_90m'',''A_HaEd_90m\n')
  nomes=['Matrix','EDGE','Core']
  c=0
  #print y
  if y!=0:
  
    for i in y:
      if i !='':
        ##print i
        f=i.split(' ')
        if '*' in f :
          break
        else:
          ##print f
          ids=f[0]
          ids=int(ids)
          ##print ids
          ha=f[1]
          ha=float(ha)
          haint=int(ha)
          haint=haint/10000
          ##print haint
          
          ##print haint
          txtreclass.write(`ids`+","+nomes[c]+','+`haint`+'\n')
          c=c+1
    
    txtreclass.close()



def txt(mapa,txtname,folder):
    grass.run_command('g.region',rast=mapa)
    os.chdir(r'F:\data\Talitha\Mapas_classificados_final\saidas_grass\saidas_2015_03_d11')
    os.chdir(folder)
    x=grass.read_command('r.stats',flags='a',input=mapa)
    y=x.split('\n')
    
    listapoio=[]
    for i in y:
        if ('*' in i):
            continue
        else:
            listapoio.append(i)
    del listapoio[-1]
    
    fd = open(txtname,'w')
    myCsvRow="Cod"",""AreaM2" ",""Area_ha\n"
    fd.write(myCsvRow)
    for i in listapoio:
        temp1=i.split(' ')
        cod=int(temp1[0])
        aream2=float(temp1[1])
        area_HA=round(aream2/10000,2)
        fd.write(`cod`+','+`aream2`+','+`area_HA`+'\n')
    fd.close()







grass.run_command('r.mask',flags='r')
lista_classificada=grass.mlist_grouped ('rast', pattern='*classificada*') ['PERMANENT']
lista_buffers=grass.mlist_grouped ('rast', pattern='*buffer*') ['PERMANENT']


escala_edge=[7,19]
for i in lista_classificada:
    os.chdir(r'F:\data\Talitha\Mapas_classificados_final\saidas_grass\saidas_2015_03_d11')
    folderveg=i[13:19]+'_veg_all'
    folderEd=i[13:19]+'_Edge_all' 
    #print   folderveg
    os.mkdir(folderveg)
    os.mkdir(folderEd)
    x=1
    for a in lista_buffers[0:4]:
        #print i,"*",a
        names_txt=a[0:12]
        apoioname=a[22:26]
        names_txt=names_txt+apoioname
        #print names_txt
        grass.run_command("g.region",rast=a)
        x=grass.read_command('r.stats',input=a)
        y=x.split('\n')
        del y[-1]
        del y[-1]
        for b in y:
            j=b
            #print b
            #print j
            name='000000'+j
            name=name[-4:]
            #print name,"*",names_txt
            txtnameveg= names_txt+'_TXTVEG_Pai_'+name+".csv"
            grass.run_command('g.region',rast=a)
            expressao1="apoio_mask=if("+a+"=="+j+",0,null())"
            grass.mapcalc(expressao1, overwrite = True, quiet = True)
            grass.run_command('r.mask',input="apoio_mask",overwrite = True)     
            expressao2="apoio2=if("+i+"==11 || "+i+"==12 || "+i+"==13  ,"+i+",0)"
            grass.mapcalc(expressao2, overwrite = True, quiet = True)
            expressao3=names_txt+'_Pai_'+name+"_FLT=if(apoio_mask==0,apoio2,null())"         
            grass.mapcalc(expressao3, overwrite = True, quiet = True)
            txt(names_txt+'_Pai_'+name+"_FLT", txtnameveg,folderveg)   
            expressao4=names_txt+'_Pai_'+name+"_FLT_bin=int(if("+names_txt+'_Pai_'+name+"_FLT>0,1,0))"
            grass.mapcalc(expressao4, overwrite = True, quiet = True)
            escalauax=''
            for t in escala_edge:
              if t==7:
                escalauax="30m"
              else:
                escalauax="90m"

              txtnameedge=names_txt+'_TXTEDGE_Pai_'+name+'_esc_'+escalauax+".csv"
              grass.run_command('r.neighbors',input=names_txt+'_Pai_'+name+"_FLT_bin",output='bintemp_dila',method='minimum',size=t,overwrite=True)
              series=names_txt+'_Pai_'+name+"_FLT_bin,bintemp_dila"
              #print '>>>>>>>>>>>>>>',series 
              grass.run_command('r.series',input=series,out='bintem_dila_edge',method="sum",overwrite=True)
              expressao5=names_txt+'_Pai_'+name+'_EDGE_'+escalauax+'=int(if('+names_txt+'_Pai_'+name+"_FLT_bin>=0,bintem_dila_edge,null()))"
              grass.mapcalc(expressao5, overwrite = True, quiet = True)  
              createtxtED(names_txt+'_Pai_'+name+'_EDGE_'+escalauax,txtnameedge,folderEd,t)
            grass.run_command('r.mask',flags='r')
            grass.run_command('g.remove',rast='apoio_mask,'+names_txt+'_Pai_'+name+"_FLT,bintemp_dila,bintem_dila_edge,apoio2") 
            
    del lista_buffers[0:4]
  

    

  