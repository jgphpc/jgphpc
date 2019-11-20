#!/bin/bash

job_nodelist="$1"
# scontrol.nodelist=$2
scontrol show nodes > eff_scontrol_nodelist 

while read nid ;do
    state=`grep -A5 "^NodeName=nid$nid" eff_scontrol_nodelist |grep State= |awk '{print $1}'`
    echo "nid$nid $state"
done < $job_nodelist | grep -v "IDLE " |grep -v ALLOCATED|sort -k2 
echo "input=$job_nodelist output=removed nodes (empty if none)"
