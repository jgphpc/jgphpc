#!/bin/bash

# export G2G=2
# srun -p dev --gres=gpu:16 -N1 -n2 --ntasks-per-node=2 -t1 ./osu_bw D D

### export CUDA_VISIBLE_DEVICES=${SLURM_LOCALID}
### export MV2_COMM_WORLD_LOCAL_RANK=${SLURM_LOCALID}

# export MV2_CUDA_IPC=0 
# export MV2_USE_GPUDIRECT=1

$@

# exit 0

uname -a
echo G2G=$G2G
echo LOCAL_RANK=$LOCAL_RANK
echo MV2_ENABLE_AFFINITY=$MV2_ENABLE_AFFINITY
echo MV2_IBA_HCA=$MV2_IBA_HCA
echo OMPI_MCA_btl_openib_if_include=$OMPI_MCA_btl_openib_if_include
echo CPULIST=$CPULIST
echo CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES
echo JOBCORES=$JOBCORES
echo MV2_COMM_WORLD_LOCAL_RANK=$MV2_COMM_WORLD_LOCAL_RANK
echo MV2_CUDA_IPC=$MV2_CUDA_IPC
echo MV2_GPUDIRECT_GDRCOPY_LIB=$MV2_GPUDIRECT_GDRCOPY_LIB==/apps/escha/gdrcopy/default/lib64/libgdrapi.so
echo MV2_USE_CUDA=$MV2_USE_CUDA
echo 2MV2_USE_GPUDIRECT=$MV2_USE_GPUDIRECT
echo 2OMP_DEFAULT_DEVICE=$OMP_DEFAULT_DEVICE
echo 3ACC_DEVICE_NUM=$ACC_DEVICE_NUM
echo 3CRAY_ACC_DEVICE=$CRAY_ACC_DEVICE
echo 4MV2_CUDA_ENABLE_MANAGED=$MV2_CUDA_ENABLE_MANAGED
echo 4MV2_CUDA_MANAGED_IPC=$MV2_CUDA_MANAGED_IPC
echo 5CUDA_AUTO_BOOST=$CUDA_AUTO_BOOST
echo 5GCLOCK=$GCLOCK
echo 6SCOREP_CUDA_ENABLE=$SCOREP_CUDA_ENABLE
echo 6MPICH_RDMA_ENABLED_CUDA=$MPICH_RDMA_ENABLED_CUDA

$@
