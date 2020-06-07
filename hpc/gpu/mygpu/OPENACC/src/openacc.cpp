// --- CSCS (Swiss National Supercomputing Center) ---
//
//
//
// -------> ~/jgphpc.git/hpc/gpu/myprogrammingmodel/myhello.c
//
//
//
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

// #include <omp.h>
// #include <mpi.h>
#ifdef _OPENACC
#include <openacc.h>
#endif

void set(double *a, double *b, double *c, int N);
void saxpy( int n, double a, double *x, double *y);
void debug();

void run(int rank, int N)
{
    // initialize application
//    MPI_Barrier(MPI_COMM_WORLD);
    double *a = reinterpret_cast<double*>(malloc(N*sizeof(double)));
    double *b = reinterpret_cast<double*>(malloc(N*sizeof(double)));
    double *c = reinterpret_cast<double*>(malloc(N*sizeof(double)));

    debug();
    set(a,b,c,N);
#ifdef _OPENACC
    int cscs_oacc_v;
    switch (_OPENACC) {
        case 201111: cscs_oacc_v=10; break;
        case 201306: cscs_oacc_v=20; break;
        case 201510: cscs_oacc_v=25; break;
        case 201711: cscs_oacc_v=26; break;
// https://www.openacc.org/sites/default/files/inline-files/OpenACC.2.6.final.pdf
        case 201811: cscs_oacc_v=27; break;
// https://www.openacc.org/sites/default/files/inline-files/OpenACC.2.7.pdf
        default:     cscs_oacc_v=_OPENACC;
    }
    printf("OpenACC/%d \n", cscs_oacc_v);
    if (acc_get_device_type() != acc_device_none){
        std::cout << "acc_get_device_type:" << acc_get_device_type() << std::endl;
    }
    std::cout << "_OPENACC version:" << _OPENACC << std::endl;    
    saxpy(N, 1.0, b, c);
#endif

    std::cout << "c[0]=" << c[0] << std::endl;
    std::cout << "c[1]=" << c[1] << std::endl;
    std::cout << "c[N/2]=" << c[N/2] << std::endl;
    std::cout << "c[N-1]=" << c[N-1] << std::endl;

    free(a);
    free(b);
    free(c);
}
 


int main(int argc, char **argv){
    // init mpi
    int rank, size;
//    MPI_Init(&argc, &argv);
//    MPI_Comm_size(MPI_COMM_WORLD, &size);
//    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    //const int N = 4600;
    int N = atoi(argv[1]);  //argv[0] is the program name
//    if(!rank) std::cout << "using MPI with " << size << " PEs, N=" << N << std::endl;
    run(rank, N);

    // finalize MPI
//    MPI_Finalize();

   return 0;
}

void set(double *a, double *b, double *c, int N) {
//    #pragma omp parallel for
    for(int i=0; i<N; i++){
        a[i] = 2.;
        b[i] = i*1.0;
        c[i] = i*100.0;
    }
}

void saxpy( int n, double a, double *x, double *y){
    #pragma acc parallel loop pcopyin(x[0:n]) pcopy(y[0:n])
    for( int i = 0; i < n; ++i )
        y[i] += a*x[i];
}

void debug()
{
    // compiler version:
    #ifdef _CRAYC
    //#define CURRENT_PE_ENV "CRAY"
    std::cout << "compiler: CCE/" << _RELEASE << "." << _RELEASE_MINOR << std::endl;
    #endif

    //std::cout << "compiler: GNU/" << <<  << std::endl;

    #ifdef __GNUC__
    //#define CURRENT_PE_ENV "GNU"
    std::cout << "compiler: GNU/" << __GNUC__ << "." << __GNUC_MINOR__
        << "." << __GNUC_PATCHLEVEL__
        << std::endl;
    #endif

    #ifdef __INTEL_COMPILER
    //#define CURRENT_PE_ENV "INTEL"
    std::cout << "compiler: INTEL/" << __INTEL_COMPILER << std::endl;
    #endif

    #ifdef __PGI
    //#define CURRENT_PE_ENV "PGI"
    std::cout << "compiler: PGI/" << __PGIC__
         << "." << __PGIC_MINOR__
         << "." << __PGIC_PATCHLEVEL__
         << std::endl;
    #endif
}
