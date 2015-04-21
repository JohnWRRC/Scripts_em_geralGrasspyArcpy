import grass.script as grass
import os
os.chdir(r'C:\_data\vivi_brito\shps_500m\Mapa_het_saidas_grass')

lista_rast=grass.mlist_grouped ('rast', pattern='*land*') ['PERMANENT']

for i in lista_rast:
    grass.run_command('g.region',rast=i)
    stats=grass.read_command('r.stats',input=i)
    ListStats=stats.split('\n')
    #print ListStats
    del ListStats[-1]
    del ListStats[-1]
    lista_multplos2=[]
    y=0
    #print len(ListStats)
    while len(ListStats)>=y:
        if y==0:
            resulti=1
        else:
            resulti=resulti*2
        lista_multplos2.append(resulti)
        y=y+1
    cont_reclasse=0
    lista_jucao_final=[]
    for sts in ListStats:
        formatname='000000'+`lista_multplos2[cont_reclasse]`
        #print formatname
        formatname=formatname[-5:]
        #print formatname
        expressao1=i+'_'+formatname+'_bin=if('+i+"=="+sts+","+`lista_multplos2[cont_reclasse]`+',0)'
        #print expressao1
        grass.mapcalc(expressao1, overwrite = True, quiet = True)
        expressao2=i+'_'+formatname+'_bin_int=int('+i+'_'+formatname+'_bin)'
        grass.mapcalc(expressao2, overwrite = True, quiet = True)
        grass.run_command('g.region',rast=i+'_'+formatname+'_bin_int')
        grass.run_command('r.neighbors',input=i+'_'+formatname+'_bin_int',out=i+'_'+formatname+'_bin_int_dila_50m',method='maximum',size=9,overwrite = True)
        cont_reclasse=cont_reclasse+1
        grass.run_command('g.remove',flags='f',rast=i+'_'+formatname+'_bin')
    lista_jucao_final=grass.mlist_grouped ('rast', pattern='*dila_50m*') ['PERMANENT'] 
    grass.run_command('r.series',input=lista_jucao_final,out='temp',overwrite = True,method='sum')
    expressao3=i+'_MapaHet_FINAL=int(if('+i+'>0,temp,null()))'
    grass.mapcalc(expressao3, overwrite = True, quiet = True)  
    grass.run_command('g.remove',flags='f',rast='temp')
    grass.run_command('r.colors',map=i+'_MapaHet_FINAL',color='wave')
    grass.run_command('r.out.gdal',input=i+'_MapaHet_FINAL',out=i+'_MapaHet_FINAL.tif')
    for rm in lista_jucao_final:
        grass.run_command('g.remove',flags='f',rast=rm)
        
     
    



    