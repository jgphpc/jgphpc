#!/bin/bash

# out=o_loop

if [ $SLURM_LOCALID = 0 ] ;then
echo "t0: `date +%Y/%m/%d-%H:%M:%S-%s.%N`" #> $out
fi

echo "SLURM_LOCALID=$SLURM_LOCALID SLURM_PROCID=$SLURM_PROCID SLURM_STEPID=$SLURM_STEPID SLURM_ARRAY_TASK_ID=$SLURM_ARRAY_TASK_ID"

sleep 5

if [ $SLURM_LOCALID = 0 ] ;then
echo "t1: `date +%Y/%m/%d-%H:%M:%S-%s.%N`" #>> $out
fi
