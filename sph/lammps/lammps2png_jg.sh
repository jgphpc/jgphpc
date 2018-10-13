#!/bin/bash

# takes lammps simulation dump (sph/water_collapse/water_collapse.lmp) as input 
# and plot the particles' position (x,y):
## ITEM:ATOMS id type xs ys zs vx vy vz 
##             1 2 0          0           0.5 0 0 0 
##             2 2 0.00176733 0.000883773 0.5 0 0 0 
## etc...

#in=$1
outtxt=eff.dump
outgp=eff.gp
ff=$1
# for ff in dump.*.lammpstrj ;do 
    nstep=`echo $ff |cut -d\. -f2 |awk '{printf "%06d",$0}'`

    sed -e '1,10d' $ff > $outtxt

cat > eff.gp <<EOF
set term png
set output "$ff.png"
set yrange [0:3]
#set yrange [0:0.3]
plot '$outtxt' u 3:(\$2==1?\$4:0) notitle w dots, '$outtxt' u 3:(\$2==2?\$4:0) title "$nstep" w dots # points
EOF

    gnuplot -c $outgp
    echo $ff
    #exit 0

# done
# rm 
