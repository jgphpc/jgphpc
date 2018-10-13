#!/bin/bash

# /apps/common/UES/sandbox/jgp/sphflow/sphynx.git/compile/timing.d.sh timing.d
in="$1"

tempf=.eff.

# --- internal timers => timing.d
#  col1  buildtree                    1 3.0657887458801270E-01
#  col2  findneighbors                2 4.5357470512390137E+00
#  col3  findneighborsMPI             3 8.2163810729980469E-02
#  col4  density*                     4 3.1072616577148438E-01
#  col5  densityMPI                   5 1.5259480476379395E-01
#  col6  xxx                          6 -1.0000000000000000E+00
#  col7  iad                          7 2.2753715515136719E-01
#  col8  iadMPI                       8 1.2966394424438477E-01
#  col9  eos                          9 2.5288105010986328E-02
#  col10 divv                        10 2.2152900695800781E-01
#  col11 divvMPI                     11 2.6065826416015625E-02
#  col12 momeqn                      12 4.6182584762573242E-01
#  col13 momeqnMPI                   13 9.6103191375732422E-02
#  col14 xxx                         14 -1.0000000000000000E+00
#  col15 xxx                         15 -1.0000000000000000E+00
#  col16 treewalk                    16 2.4877595901489258E-01
#  col17 treewalkMPI                 17 6.2780380249023438E-03
#  col18 update                      18 1.3627244949340820E+01
#  col19 timectrl                    19
#  col20 output                      20

buildtree         
findneighbors     
findneighborsMPI  
density*          
densityMPI        
xxx               
iad               
iadMPI            
eos               
divv              
divvMPI           
momeqn            
momeqnMPI         
xxx               
xxx               
treewalk          
treewalkMPI       
update            
timectrl          
output            

buildtree         
findneighbors     
density*          
iad               
eos               
divv              
momeqn            
treewalk          
update            
timectrl          

# --- internal timers => timing.d
#  col1  !1 - Communications for Gravity    1  commforG
#  col2  !2. buildtree                      2  BuildTree
#  col3  !3. treewalk (Gravity calculation) 3  TreewalkG
#  col4  !4 - Internal gravity comm.        4  commInternalG
#  col5  !5. findneighbors                  5  findNeighbors
#  col6  !6. calculate_density              6  calcdensity
#  col7  !7 - Neighbors comm                7  commNeighbors
#  col8  !8 - Density comm                  8  commDensity
#  col9  !9 calculate_IAD                   9  calcIAD
#  col10 !10 - IAD terms comm              10  commIAD
#  col11 !11 eostot                        11  eos
#  col12 !13 calculate_divv                12  calcDivv
#  col13 !14 - Div-v comm                  13  commDivv
#  col14 !15 momeqn - Mom + Energy eqs     14  mom+energyEqn
#  col15 !16 - Mom + Energy eqs comm       15  commMom+Energy
#  col16 !17 - Communications from gravity 16  commfromG
#  col17 !18 - update                      17  update


# --- sum
niterations=15

for col in `seq 17` ;do 
    nrows=`wc -l $in |awk '{print $1}'`
    if [ $nrows -ne $niterations ] ; then
        echo "nrows=$nrows /= $niterations !!!"
        exit -1
    fi
    s=`awk '{s=s+$'$col'}END{print s/'$niterations'}' $in`
    echo $col $s
done # > $tempf 

# total=`awk '{s=s+$2}END{print s}' $tempf`
# awk -v t=$total '{printf "%s %.4f%%\n",$0,$2/t*100}' $tempf
