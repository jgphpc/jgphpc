#!/bin/bash

# 6462849  nid0[0115-0121,1563-1564]

cn=$1
otmp=.eff.$$
SQUEUE_FORMAT="%8i %N" squeue -t R &> $otmp

while read jid cnlist ;do
    echo -n .
    cns=`hostlist -e $cnlist`
    echo $jid $cns |grep $cn
done < $otmp
