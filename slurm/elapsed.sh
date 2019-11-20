#!/bin/bash

SLURM_TIME_FORMAT=%Y/%m/%d-%H:%M:%S
for f in slurm-*.out ;do 
    x=`echo $f| cut -c7-12`
    sacct  --format=JobID,Start,End,Elapsed,JobName -j $x  
done 
# |grep NVIDIA-Te
