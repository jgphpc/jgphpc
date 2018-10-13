#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=12  # -N
#SBATCH --cpus-per-task=1     # -d/-c openmp
#SBATCH --ntasks-per-core=1   # -j
#SBATCH --hint=nomultithread
#
#SBATCH --time=00:01:00
#SBATCH --job-name="x"
#SBATCH --output=effo_
#SBATCH --error=effo_
#SBATCH -C gpu

echo '# -----------------------------------------------'
ulimit -c unlimited
ulimit -s unlimited
ulimit -a |awk '{print "# "$0}'
export OMP_NUM_THREADS=1
echo "# SLURM_JOBID = $SLURM_JOBID"
echo CRAY_CUDA_MPS=$CRAY_CUDA_MPS
echo HUGETLB_DEFAULT_PAGE_SIZE=$HUGETLB_DEFAULT_PAGE_SIZE
echo HUGETLB_MORECORE=$HUGETLB_MORECORE
date

njobs=$SLURM_NNODES
for nnn in `seq -w $njobs` ;do
    dirn=$njobs-_job$nnn ;mkdir -p $dirn ;rm -f $dirn/*
done

set -x
for nnn in `seq -w $njobs` ;do
    dirn=$njobs-_job$nnn 
    cd $dirn

/usr/bin/time -p \
srun \
--exclusive \
-O -N 1 \
--ntasks=12 \
--ntasks-per-node=$SLURM_NTASKS_PER_NODE \
--cpus-per-task=$SLURM_CPUS_PER_TASK \
--ntasks-per-core=$SLURM_NTASKS_PER_CORE \
--hint=nomultithread \
--cpu_bind=rank \
../CRAY &> o_$dirn &

    cd -

done

wait

set +x
exit 0
