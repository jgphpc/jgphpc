#!/bin/bash

# scn --oneline > eff.scn
# in=eff.scn

in=$1
echo "cn free real alloc state c"
while read line ;do
    noden=`echo $line |cut -d= -f2 |cut -d " " -f1`

    freemem=`echo $line |awk -F"FreeMem=" '{print $2}' |cut -d= -f1 |cut -d" " -f1`
    realmem=`echo $line |awk -F"RealMemory=" '{print $2}' |cut -d= -f1 |cut -d" " -f1`
    allocmem=`echo $line |awk -F"AllocMem=" '{print $2}' |cut -d= -f1 |cut -d" " -f1`
    state=`echo $line |awk -F"State=" '{print $2}' |cut -d= -f1 |cut -d" " -f1`
    cores=`echo $line |awk -F"CPUTot=" '{print $2}' |cut -d= -f1 |cut -d" " -f1`
    echo $noden $freemem $realmem $allocmem $state $cores

    #freemem=`echo $line |cut -d= -f18 |cut -d " " -f1`
    #realmem=`echo $line |cut -d= -f16 |cut -d " " -f1`
    #state=`echo $line |cut -d= -f21 |cut -d " " -f1`
    #diffmem=`echo $realmem $freemem |awk '{printf "%d",$1-$2}'`
    #echo $noden $freemem $realmem $diffmem $state

done < $in
