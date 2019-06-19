// /apps/common/UES/sandbox/jgp/openmp/sollve_vv.git/tests/4.5/offloading_success.cpp
#include <stdio.h>
#include <omp.h>
#include <iostream>

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

int main(void) {
  int isHost = 0;

#pragma omp target map(from: isHost)
  { isHost = omp_is_initial_device(); }

  if (isHost < 0) {
    printf("Runtime error, isHost=%d\n", isHost);
  } else {
    int num_dev = omp_get_num_devices();
    printf("num_devices=%d\n", num_dev);
  }

  // CHECK: Target region executed on the device
  printf("Target region executed on the %s\n", isHost ? "host" : "device");

  // openmp support:
  int tid, nthreads;
  #pragma omp parallel private(tid, nthreads)
  {
    tid = omp_get_thread_num();
    nthreads = omp_get_num_threads();
    #pragma omp critical
    {
      printf("# thread %d / %d %d\n", tid, nthreads, _OPENMP);
    }
  }

  debug();

  return isHost;
}
