#!/bin/bash

#for i in 04 08 12 16; do 
in=$1
    grep JOBID $in \
        |awk '{print "sacct --format=elapsed -j "$4}' \
        |sh \
        |grep -m1 : \
        |awk '{print "/users/piccinal/linux.git/slurm/2seconds.sh ",$0}'
 
#   done |awk '{print "/users/piccinal/linux.git/slurm/2seconds.sh ",$0}'


