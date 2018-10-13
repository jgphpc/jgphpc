#!/bin/bash

# RUNJG="srun -Q -n1 -t1 -C mc"
RUNJG="srun -Q -n1 -t1 -C gpu"

# for i in ascii png fig synthetic console xml fig ; do 
for i in ascii png synthetic ;do
    $RUNJG \
    lstopo --no-io --of $i > o_$i 
    echo $i 
done

