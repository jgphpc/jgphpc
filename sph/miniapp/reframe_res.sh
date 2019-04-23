#!/bin/bash

weak="F"
strong="T"

 #    #  ######    ##    #    #
 #    #  #        #  #   #   #
 #    #  #####   #    #  ####
 # ## #  #       ######  #  #
 ##  ##  #       #    #  #   #
 #    #  ######  #    #  #    #
# --- weak:
if [ $weak = "T" ];then
# xsteps=60
xsteps=40
in=$1

fn=`basename $in`
echo -n "$fn "
dn=`dirname $in`
mpit=`echo $dn |awk -F_ '{printf "%d\n", substr($4,0,6)}'`
cn=`echo $mpit |awk '{print $0/12}'`
ompt=`echo $dn |awk -F_ '{print substr($5,0,1)}'`
compilerv=`echo $dn |awk -F_ '{print $3}'`
cpubind=`echo $dn|awk -F-cc '{print $2}'|cut -d_ -f1`
if [ -z $cpubind ]; then cpubind="empty"; fi

steps=`grep '=== Total time for iteration' $in |wc -l`
elapsedtime=`grep '=== Total time for iteration' $in |head -$xsteps |awk '{s=s+$6}END{print s}'`
timeperstep=`grep '=== Total time for iteration' $in |head -$xsteps |awk '{s=s+$6}END{print s/NR}'`

echo "@$mpit @$ompt @$steps @$xsteps @$cn @$elapsedtime @$timeperstep @$compilerv @$cpubind" |tr -d " "
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
