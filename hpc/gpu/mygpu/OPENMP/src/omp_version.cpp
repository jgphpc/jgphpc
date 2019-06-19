/*
* https://github.com/eth-cscs/reframe/blob/master/cscs-checks/tools/profiling_and_debugging/notool.py#L43
*         self.openmp_versions = ScopedDict({
*            'PrgEnv-intel': {'version': 201611},
*            'PrgEnv-cray': {'version': 201511},
*            'PrgEnv-gnu': {'version': 201511},
*            'PrgEnv-pgi': {'version': 201307},
*/
// ~/reframe.git/cscs-checks/prgenv/src/hello_world_openmp.cpp
/*
* intel/19.0.1: CC -qopenmp omp_version.cpp && srun -Cgpu -t1 -n1 ./a.out # 201611 
* cce/8.7.9: CC -homp omp_version.cpp && srun -Cgpu -t1 -n1 ./a.out # 201511
* cce/9.0.0: CC -homp omp_version.cpp && srun -Cgpu -t1 -n1 ./a.out # 201511
* gcc/7.3.0: CC -fopenmp omp_version.cpp && srun -Cgpu -t1 -n1 ./a.out # 201511
* gcc/8.3.0: CC -fopenmp omp_version.cpp && srun -Cgpu -t1 -n1 ./a.out # 201511
* pgi/18.10.0: CC -mp omp_version.cpp && srun -Cgpu -t1 -n1 ./a.out # 201307
*/

#include <stdio.h>   
#include <omp.h>
 
int main(int argc, char *argv[])
{
  int tid, nthreads;
  #pragma omp parallel private(tid, nthreads)
  {
    tid = omp_get_thread_num();
    nthreads = omp_get_num_threads();
    #pragma omp critical
    {
      // printf("thread %d / %d \n", tid, nthreads);
      printf("# thread %d / %d %d\n", tid, nthreads, _OPENMP);
    }
  }
 
  return 0;
}
