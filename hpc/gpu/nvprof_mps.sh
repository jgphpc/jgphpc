#!/bin/bash

if [ $SLURM_LOCALID -eq 0 ] ;
then
   host=`hostname`
   export TMPDIR=$PWD/$SLURM_TASK_PID
   mkdir -p $TMPDIR
   echo "Launching profiler on $host"
   nvprof --profile-all-processes  --export-profile profile_%p.prof &
fi

sleep 1

$1
