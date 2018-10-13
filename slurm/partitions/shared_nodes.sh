#!/bin/bash

# PartitionName=debug
#    Nodes=nid0[0008-0011
# 
# PartitionName=prepost
#    Nodes=nid0[0008-0062,

function nodelist() {

line=$1
out=$2

# blocks_of_nodes=`echo $in |sed "s-\[-\n-g" |grep -v nid |tr -d \] |sed "s-,-\n-g"`
# for line in $blocks_of_nodes ;do

    start=`echo $line |cut -d- -f1`
      end=`echo $line |cut -d- -f2`
    if [ "$start" = "$end" ] ; then
        echo $start
    else
        echo seq $start $end |sh 
    fi

# done |awk '{printf "nid%05d\n",$0}' > eff.sharednodes.$out

}

partition_list=`scontrol show partition |grep PartitionName= |cut -d= -f2 |sort |grep -v xfer`
# partition_list=prepost

for p in $partition_list ;do
    echo $p
    # nodelist_of_partition=`scontrol show partition $p |grep " Nodes=" |cut -d= -f2 |sed "s-,nid-nid\n-g"`
    nodelist_of_partition=`scontrol show partition $p |grep " Nodes=" |cut -d= -f2 |sed "s-nid-\nnid\n-g" |grep -v nid |cut -d \[ -f2 |tr -d \] |tr \, "\n" |grep -v ^$`

    for nl in $nodelist_of_partition ;do
        nodelist $nl $p
    done |awk '{printf "nid%05d\n",$0}' |sort > eff.sharednodes.$p
    echo
done

# set -x
for p in `echo $partition_list |sed "s-debug--"` ;do
    echo "Is $p sharing nodes with debug partition ?"
    comm -12 eff.sharednodes.debug eff.sharednodes.$p
done
# set +x
