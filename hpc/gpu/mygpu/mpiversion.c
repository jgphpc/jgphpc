// --- CSCS (Swiss National Supercomputing Center) ---
#define _MPI

#include <stdio.h>
#ifdef _MPI
#include <mpi.h>
#endif
#include <unistd.h>
#include <stdlib.h>

#ifndef DEVS_PER_NODE
#define DEVS_PER_NODE 1  // Devices per node
#endif

int main(int argc, char *argv[])
{
    int rank=0, size=0, namelen;
    int mpiversion=0, mpisubversion=0;
    int resultlen = -1;
    char mpilibversion[MPI_MAX_LIBRARY_VERSION_STRING];

#ifdef _MPI
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    MPI_Init (&argc, &argv);
    MPI_Comm_rank (MPI_COMM_WORLD, &rank);  
    MPI_Comm_size (MPI_COMM_WORLD, &size);  
    // MPI_Get_processor_name(processor_name, &namelen);
    MPI_Get_version(&mpiversion, &mpisubversion);
    MPI_Get_library_version(mpilibversion, &resultlen);
        // MPICH_VERSION
        // CRAY_MPICH_VERSION
    printf("MPI_Get_version === %d.%d\n", mpiversion, mpisubversion);
    printf("MPI_Get_library_version === %s\n", mpilibversion);
#else
    char processor_name[3] = "nid";
#endif
    int dev = rank % DEVS_PER_NODE;
#ifdef _MPI
    MPI_Finalize();
#endif

    return 0;
}

/*
MPI_Get_version === 3.1
MPI_Get_library_version === MPI VERSION    : CRAY MPICH version 7.5.0 (ANL base 3.2rc1)
MPI BUILD INFO : Built Fri Oct 21 13:35:57 2016 by jemison (git hash 1cb66d6) MT-G
*/

/*
export LD_LIBRARY_PATH=$CRAY_LD_LIBRARY_PATH:$LD_LIBRARY_PATH
cc -g mpiversion.c &&  srun -n1 -Cgpu ./a.out
    MPI_Get_version === 3.1
    MPI_Get_library_version === MPI VERSION    : CRAY MPICH version 7.6.0 (ANL base 3.2)
    MPI BUILD INFO : Built Wed Jun 21 13:29:06 2017 (git hash 0a738ef) MT-G
*/
