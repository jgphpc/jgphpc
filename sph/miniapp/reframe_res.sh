#!/bin/bash

weak="T"
strong="F"
cpubind="F"

#    #  ######    ##    #    #
#    #  #        #  #   #   #
#    #  #####   #    #  ####
# ## #  #       ######  #  #
##  ##  #       #    #  #   #
#    #  ######  #    #  #    #
# --- weak:
if [ $weak = "T" ];then
# xsteps=60
xsteps=41
in=$1

fn=`basename $in`
dn=`dirname $in`
# echo -n "$fn "
mpit=`echo $dn |awk -F_ '{printf "%d\n", substr($4,0,6)}'`
cn=$mpit
# cn=`echo $mpit |awk '{print $0/12}'`
# ompt=`echo $dn |awk -F_ '{print substr($5,0,1)}'`
openmp_threads=`grep -m1 "OPENMP: version" $in |awk '{print $4}'`

#compilerv=`echo $dn |awk -F_ '{print $3}'`
# cpubind=`echo $dn|awk -F-cc '{print $2}'|cut -d_ -f1`
# if [ -z $cpubind ]; then cpubind="empty"; fi
mpi_version=`grep -m1 "CRAY MPICH version" $in |awk '{print "mpi/"$9}'`
openmp_version=`grep -m1 "OPENMP: version" $in |awk '{print $3}' |cut -d/ -f2 |awk '{print "omp/"$0}'`
compiler_version=`grep -m1 "COMPILER: " $in |awk '{print $3}'`

steps=`grep '=== Total time for iteration' $in |wc -l`
elapsedtime=`grep '=== Total time for iteration' $in |head -$xsteps |awk '{s=s+$6}END{print s}'`
timeperstep=`grep '=== Total time for iteration' $in |head -$xsteps |awk '{s=s+$6}END{print s/NR}'`

# echo "@$mpit @$ompt @$steps @$xsteps @$cn @$elapsedtime @$timeperstep @$compilerv @$cpubind" |tr -d " "
# $in mpi	omp	steps	Steps Used	cn	elapsed time 40 first steps (seconds)
echo "$fn @$mpit @$openmp_threads @$steps @$xsteps @$cn @$elapsedtime @$timeperstep @$mpi_version @$openmp_version @$compiler_version" |tr -d " "

fi

 ####    #####  #####    ####   #    #   ####
#          #    #    #  #    #  ##   #  #    #
 ####      #    #    #  #    #  # #  #  #
     #     #    #####   #    #  #  # #  #  ###
#    #     #    #   #   #    #  #   ##  #    #
 ####      #    #    #   ####   #    #   ####
# --- strong:
if [ $strong = "T" ];then
xsteps=95
in=$1

fn=`basename $in`
echo -n "$fn "
dn=`dirname $in`
mpit=`echo $dn |cut -d_ -f4|sed "s-mpi--"`
cn=`echo $mpit |awk '{print $0/12}'`
ompt=`echo $dn |cut -d_ -f5 |cut -d- -f1 |sed "s-omp--"`
compilerv=`echo $dn |awk -F_ '{print $3}'`
cpubind=`echo $dn|awk -F-cc '{print $2}'|cut -d_ -f1`
if [ -z $cpubind ]; then cpubind="empty"; fi

steps=`grep '=== Total time for iteration' $in |wc -l`
elapsedtime=`grep '=== Total time for iteration' $in |head -$xsteps |awk '{s=s+$6}END{print s}'`
timeperstep=`grep '=== Total time for iteration' $in |head -$xsteps |awk '{s=s+$6}END{print s/NR}'`

echo "@$mpit @$ompt @$steps @$xsteps @$cn @$elapsedtime @$timeperstep @$compilerv @$cpubind" |tr -d " "

# echo "@$mpit @$ompt @$timeperstep @$compilerv @$cpubind" |tr -d " "
# echo $mpit $ompt $timeperstep $compilerv $cpubind
fi


  ####   #####   #    #  #####      #    #    #  #####
 #    #  #    #  #    #  #    #     #    ##   #  #    #
 #       #    #  #    #  #####      #    # #  #  #    #
 #       #####   #    #  #    #     #    #  # #  #    #
 #    #  #       #    #  #    #     #    #   ##  #    #
  ####   #        ####   #####      #    #    #  #####
# --- cpubind:
if [ $cpubind = "T" ];then
xsteps=35
# xsteps=18
# xsteps=5
in=$1

fn=`basename $in`
echo -n "$fn "
dn=`dirname $in`
mpit=`echo $dn |cut -d_ -f4|sed "s-mpi--"`
cn=1
ompt=`echo $dn |cut -d_ -f5 |cut -d- -f1 |sed "s-omp--"`
compilerv=`echo $dn |awk -F_ '{print $3}'`
cpubind=`echo $dn|awk -F-cc '{print $2}'|cut -d_ -f1`
if [ -z $cpubind ]; then cpubind="empty"; fi

steps=`grep '=== Total time for iteration' $in |wc -l`
elapsedtime=`grep '=== Total time for iteration' $in |head -$xsteps |awk '{s=s+$6}END{print s}'`
timeperstep=`grep '=== Total time for iteration' $in |head -$xsteps |awk '{s=s+$6}END{print s/NR}'`

echo "@$mpit @$ompt @$steps @$xsteps @$cn @$elapsedtime @$timeperstep @$compilerv @$cpubind" |tr -d " "

# echo "@$mpit @$ompt @$timeperstep @$compilerv @$cpubind" |tr -d " "
# echo $mpit $ompt $timeperstep $compilerv $cpubind
fi
