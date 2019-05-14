# Cray XC nodes - 2 x 18-cores Intel E5-2695 v4 'Broadwell' processors
# https://www.cscs.ch/computers/piz-daint/ (@2.10GHz, 64/128 GB RAM)

ERT_ALIGN               32
ERT_CC                  cc
ERT_CFLAGS              -O3 -Ofast
# -Mipa=fast -fno-alias -fno-fnalias -axAVX -xAVX -DERT_INTEL
ERT_DRIVER              driver1
ERT_FLOPS               1,2,4,8,16,32,64,128,256,512,1024 
# see ERT_ in kernel1.c
ERT_GNUPLOT             gnuplot

#ERT_GPU                 True
#ERT_GPU_BLOCKS          56,112,448,896,1792 # (P100)
#ERT_GPU_CFLAGS          -x cu
#ERT_GPU_LDFLAGS         
#ERT_GPU_THREADS         64,128,256,512,1024 # (P100)
#ERT_BLOCKS_THREADS      114688 # (P100 Peak number of threads)

ERT_KERNEL              kernel1
ERT_LD                  cc
ERT_LDFLAGS             
ERT_LDLIBS              
# 1024^3 = 1073741824 = 1GB
ERT_MEMORY_MAX          1073741824

# --- MPI:
ERT_MPI                 True
ERT_MPI_CFLAGS          
ERT_MPI_LDFLAGS         
ERT_MPI_PROCS           36
# ERT_MPI_PROCS           1,2,4,8,12,18,24,36
ERT_NUM_EXPERIMENTS     2

# --- OPENMP:
ERT_OPENMP              True
ERT_OPENMP_CFLAGS       -fopenmp
ERT_OPENMP_LDFLAGS      -fopenmp
ERT_OPENMP_THREADS      1-36

# --- MPI * OPENMP = mpi*omp
ERT_PROCS_THREADS       36 

#                       mkdir /scratch/snx3000tds/piccinal/Results.dom-mc.cscs.ch/
ERT_RESULTS             /scratch/snx3000tds/piccinal/Results.dom-mc.cscs.ch/gnu73
#ERT_RUN                ERT_CODE  # sbatch
ERT_RUN                 export OMP_NUM_THREADS=ERT_OPENMP_THREADS; srun -Cmc -t5 --ntasks=ERT_MPI_PROCS --ntasks-per-node=ERT_MPI_PROCS --cpus-per-task=ERT_OPENMP_THREADS --ntasks-per-core=1 --hint=nomultithread --cpu_bind=verbose,none ERT_CODE

#ERT_SPEC_GBYTES_DRAM    0.0
#ERT_SPEC_GBYTES_L1      0.0
#ERT_SPEC_GFLOPS         0.0
ERT_TRIALS_MIN          1
ERT_WORKING_SET_MIN     1 # 128 # ?

# --------------------------------
##ERT_SPEC_GBYTES_DRAM   102.40
##ERT_SPEC_GBYTES_L1    1843.20
##ERT_SPEC_GFLOPS        460.40
