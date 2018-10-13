#!/bin/bash

# ./run.sh 1 1 12 1 verbose,rank ./GNU.haswell.test.mpi

export OMP_NUM_THREADS=$3

case $4 in
    0) mth="--ntasks-per-core=1" ;;
    1) mth='--ntasks-per-core=1 --hint=nomultithread' ;;
    2) mth='--ntasks-per-core=2 --hint=multithread' ;;
    *) break ;;
esac
echo mth=$mth

set -x 
srun -Cmc \
-n$1 \
--ntasks-per-node=$2 \
-c $OMP_NUM_THREADS \
$mth \
--cpu_bind=$5 \
$6
set +x
