#!/bin/bash

# scn --oneliner > eff.scn

in=$1
while read line ;do
    noden=`echo $line |cut -d= -f2 |cut -d " " -f1`
    features=`echo $line |sed "s-ActiveFeatures=-\nActiveFeatures=-g" |grep ^ActiveFeatures= |awk '{print $1}'`
    cputot=`echo $line |cut -d= -f7 |cut -d " " -f1`
    state=`echo $line |cut -d= -f21 |cut -d " " -f1`
    echo $noden $state $cputot $features |awk '{printf "%10s %10s %6d %20s\n",$1,$2,$3,$4}'
done < $in

#  nid00000   RESERVED     24 ActiveFeatures=gpu,startx,c0-0,group0,row0,mon,gpumodedefault
#  nid00001       IDLE     24 ActiveFeatures=gpu,startx,c0-0,group0,row0,mon,gpumodedefault

