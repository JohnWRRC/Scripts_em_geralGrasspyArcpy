import os
import fnmatch
import sys

os.chdir("F:/data/Juliana_inpe/RESULTADOS_Smmal_Mammals/juliana_teste")


lista=[]
lista=os.listdir("F:/data/Juliana_inpe/RESULTADOS_Smmal_Mammals/juliana_teste")

os.getcwd()


arquivo = open('soma_geral.bat', 'w')
for i in lista:
    temp=i
   
    
    if temp=="hm":
        linha1= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\\"+temp+ "\n"
        linha2="list=`g.mlist pattern=\"*sem0\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_abertas_"+temp+" method=sum""\n" 
        linha3="list=`g.mlist pattern=\"*soma_abertas_"+temp+"\" sep=\"comma\"`" "\n" "g.region rast=$list" "\n" "r.grow.distance in=$list out=distance_abertas_"+temp+" -m" "\n"
        
        linha4="\n" "cd \"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\saidas\""
        linha5="\n""listaex=`g.mlist pattern=\"*distance\"`" "\n" "for i in $" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\"_Bin"",""_Bin.tif\");print}'`" "\n" "r.out.gdal in=$a out=$out format=GTiff nodata=-9999 --v" "\n" "done" "\n"        
        linhaaux="#..................................................................................................................................................................""\n"
        arquivo.write(linha1)
        arquivo.write(linha2)
        arquivo.write(linha3)
        arquivo.write(linha4)
        arquivo.write(linha5)
        arquivo.write( linhaaux) 
      
    if temp=="AF" or temp=="Het":
        linha6= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\\"+temp+ "\n"
        linha7="list=`g.mlist pattern=\"*sem0\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_abertas"+temp+" method=sum" "\n"
        linha8= "llist=`g.mlist pattern=\"soma*\"`" "\n" "r.mapcalc \"$list\"_Bin\"=if($list<1,null(),1)\" " "\n"
        linhaaux="#..................................................................................................................................................................""\n"
        linha9="\n" "cd \"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\saidas\""
        linha10="\n""listaex=`g.mlist pattern=\"_Bin*\"`" "\n" "for i in $listaex" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\"_Bin"",""_Bin.tif\");print}'`" "\n" "r.out.gdal in=$a out=$out format=GTiff nodata=-9999 --v" "\n" "done" "\n"         
        arquivo.write(linha6)
        arquivo.write(linha7)
        arquivo.write(linha8)
        arquivo.write( "\n")
        arquivo.write(linha9)
        arquivo.write(linha10)
        arquivo.write( linhaaux)
           
linha11= "\n""g.mapset -c mapset=PERMANENT location=newLocation gisdbase=\"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\saidas\" ""\n"
linha12="cd \"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\Imagens_Binarias_Distance\bins_het\""
linha13="\n" "files=*.tif" "\n" "for i in $files" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\".tif\",\"_tif\");print}'\`" "\n" "r.in.gdal in=$i out=$out -o --o" "\n" "done" "\n"
arquivo.write(linha11) 
arquivo.write(linha12)  
arquivo.write(linha13) 
arquivo.write( linhaaux)

geral=os.listdir("F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\hm")

sub='flo_af'
sub2='flo_het'
sub3='distance'

het= []
af=[]
dista=[]

for i in geral:
    if sub in i:
        print i
        af.append(i)
    elif sub2 in i:
            het.append(i)
    elif sub3 in i:
        dista.append(i)

mapdist=[]
fname=[]
con=0

for fname in af:
    ofile2=unicode(""+os.path.splitext(fname)[0]+"_final")
    
    mapdist=dista[con]
    linha14="g.region rast="+ fname +" " "res=28.5" "\n" "r.mapcalc "+ofile2+"="+fname + "*" +mapdist+ "\n" 
    con=con+1  
    arquivo.write(linha14) 
    linha14=""
        
con=0 
arquivo.write( linhaaux)
for fname in het:
    ofile2=unicode(""+os.path.splitext(fname)[0]+"_final")
        
    mapdist=dista[con]
    linha15="g.region rast="+ fname +" " "res=28.5" "\n" "r.mapcalc "+ofile2+"="+fname + "*" +mapdist+ "\n" 
    con=con+1  
    arquivo.write(linha15) 
    linha15=""




arquivo.close() 

 