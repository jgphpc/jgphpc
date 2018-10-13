#!/bin/bash

# https://webrt.cscs.ch/Ticket/Display.html?id=26258

#SBATCH -C gpu
#SBATCH -p debug
#SBATCH --nodes=1                 # -n
#SBATCH --cpus-per-task=1         # -d/-c openmp
#SBATCH --ntasks-per-core=1       # -j
#SBATCH --hint=nomultithread
#
#SBATCH --time=00:01:00
#SBATCH --job-name="staff"
#SBATCH --output=o
#SBATCH --error=o

out=o_stats
rm -f $out
date

srun \
--overcommit  --oversubscribe --relative=0 --gres=craynetwork:1,gpu:1 \
-n1 \
nvidia-smi stats -i 0 -d gpuUtil --count 10 > $out 2>&1 &

echo "# --- monitoring started"
echo

srun \
--overcommit --oversubscribe --relative=0 --gres=craynetwork:1,gpu:1 \
-n1 \
./nvprof_check &

wait 
date

