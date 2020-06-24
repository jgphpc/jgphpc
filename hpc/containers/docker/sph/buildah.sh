#!/bin/bash
#SBATCH --job-name="rfm_BuildahMpichOSUTest_job"
#SBATCH --ntasks=1
#SBATCH --output=o
#SBATCH --error=o
#SBATCH --time=1:0:0
#SBATCH --constraint=gpu,gpu,contbuild
#SBATCH --nodes=1

module load daint-gpu
module load Buildah
buildah --version

srun buildah bud --root=/scratch/local/$USER/buildah_root \
--runroot=/scratch/local/$USER/buildah_runroot --storage-driver=vfs \
--tag=mpich:eff -f \
~/jgphpc.git/hpc/containers/docker/sph/ub1804_cuda102_mpich314_gnu8.dockerfile \
.

srun buildah push --root=/scratch/local/$USER/buildah_root \
--runroot=/scratch/local/$USER/buildah_runroot --storage-driver=vfs mpich:eff \
docker-archive:/scratch/local/$USER/buildah_runroot/eff.tar

#buildah bud --root=/scratch/local/$USER/buildah_root --runroot=/scratch/local/$USER/buildah_runroot --storage-driver=vfs --tag=mpich_osu:latest -f Dockerfile_osu .
#buildah push --root=/scratch/local/$USER/buildah_root --runroot=/scratch/local/$USER/buildah_runroot --storage-driver=vfs mpich_osu:latest docker-archive:/scratch/local/$USER/buildah_runroot/mpich_osu.tar

cp /scratch/local/$USER/buildah_runroot/eff.tar .
