#!/bin/bash

#SBATCH -C gpu
##SBATCH -p debug
#SBATCH --nodes=1                 # 
#SBATCH --ntasks=2                # -n
#SBATCH --cpus-per-task=1         # -d/-c openmp
#SBATCH --ntasks-per-core=1       # -j
#SBATCH --hint=nomultithread
#
#SBATCH --time=00:01:00
#SBATCH --job-name="x"
#SBATCH --output=o
#SBATCH --error=o

module rm xalt 

which icc
srun -n1 icc -V
which advixe-cl
#export INTEL_LICENSE_FILE=

echo T: `date +%Y/%m/%d-%H:%M:%S-%s.%N`

srun --multi-prog ./mpmd+survey.conf

echo T: `date +%Y/%m/%d-%H:%M:%S-%s.%N`
