# Cray/XC40 Two Intel Xeon E5-2695 v4 Broadwell @ 2.10GHz (2 x 18 cores, 64/128 GB RAM)
# https://www.cscs.ch/computers/piz-daint/

ERT_RESULTS /scratch/snx3000tds/piccinal/ert/dom-mc/gnu
#/Run.001

#ERT_SPEC_GBYTES_L1    1843.20
#ERT_SPEC_GBYTES_DRAM   102.40
#ERT_SPEC_GFLOPS        460.40

ERT_DRIVER  driver1
ERT_KERNEL  kernel1

ERT_MPI         True
ERT_MPI_CFLAGS
ERT_MPI_LDFLAGS

ERT_OPENMP         True
ERT_OPENMP_CFLAGS  -fopenmp
ERT_OPENMP_LDFLAGS -fopenmp

ERT_FLOPS   1,2,4,8,12,18,24,36
ERT_ALIGN   32
ERT_CC      cc
ERT_CFLAGS  -O3 -Ofast 
# -Mipa=fast
# -fno-alias -fno-fnalias -axAVX -xAVX -DERT_INTEL
ERT_LD      cc
ERT_LDFLAGS 
ERT_LDLIBS  

# ERT_RUN     export OMP_NUM_THREADS=ERT_OPENMP_THREADS; srun -n ERT_MPI_PROCS -N ERT_MPI_PROCS -d ERT_OPENMP_THREADS -S `expr ERT_MPI_PROCS / 2` -ss -cc numa_node ERT_CODE
ERT_RUN     export OMP_NUM_THREADS=ERT_OPENMP_THREADS; srun --ntasks=ERT_MPI_PROCS --ntasks-per-node=ERT_MPI_PROCS --cpus-per-task=ERT_OPENMP_THREADS --ntasks-per-core=1 --hint=nomultithread -Cmc --cpu_bind=verbose ERT_CODE

ERT_PROCS_THREADS  36
ERT_MPI_PROCS      1,2,4,8,12,18,24,36
ERT_OPENMP_THREADS 1-36

ERT_NUM_EXPERIMENTS 5
ERT_MEMORY_MAX 1073741824
ERT_WORKING_SET_MIN 1
ERT_TRIALS_MIN 1
ERT_GNUPLOT gnuplot
