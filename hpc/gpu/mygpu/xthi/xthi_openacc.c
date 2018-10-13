#define _GNU_SOURCE

#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sched.h>
#include <mpi.h>
#include <omp.h>
#ifdef _OPENACC
#include <openacc.h>
#endif

/* Borrowed from util-linux-2.13-pre7/schedutils/taskset.c */

static char *cpuset_to_cstr(cpu_set_t *mask, char *str)
{
  char *ptr = str;
  int i, j, entry_made = 0;
  for (i = 0; i < CPU_SETSIZE; i++) {
    if (CPU_ISSET(i, mask)) {
      int run = 0;
      entry_made = 1;
      for (j = i + 1; j < CPU_SETSIZE; j++) {
        if (CPU_ISSET(j, mask)) run++;
        else break;
      }
      if (!run)
        sprintf(ptr, "%d,", i);
      else if (run == 1) {
        sprintf(ptr, "%d,%d,", i, i + 1);
        i++;
      } else {
        sprintf(ptr, "%d-%d,", i, i + run);
        i += run;
      }
      while (*ptr != 0) ptr++;
    }
  }
  ptr -= entry_made;
  *ptr = 0;
  return(str);
}

int main(int argc, char *argv[])
{
  int rank, thread;
  cpu_set_t coremask;
  char clbuf[7 * CPU_SETSIZE], hnbuf[64];

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  memset(clbuf, 0, sizeof(clbuf));
  memset(hnbuf, 0, sizeof(hnbuf));
  (void)gethostname(hnbuf, sizeof(hnbuf));

  // Define a prefix for the binding lines.
  char prefix[200];
  if (argc > 1)
    //   If something is specified on the command line, use that. 
    snprintf(prefix,sizeof(prefix),"%s:",argv[1]);
  else
    //   Otherwise use a generic string.
    strcpy(prefix,"Hello world from");

#ifdef _OPENACC
  int ngpus, mygpu;
  ngpus = acc_get_num_devices( acc_device_default );
  mygpu = acc_get_device_num ( acc_device_default );
#endif  

  #pragma omp parallel private(thread, coremask, clbuf)
  {
    thread = omp_get_thread_num();
    (void)sched_getaffinity(0, sizeof(coremask), &coremask);
    cpuset_to_cstr(&coremask, clbuf);
    #pragma omp barrier
#ifdef _OPENACC
    printf("%s %d, thread %d, gpu %d (of %d), on %s. (core affinity = %s)\n",
	   prefix, rank, thread, mygpu, ngpus, hnbuf, clbuf);
#else
    printf("%s %d, thread %d,               on %s. (core affinity = %s)\n",
	   prefix, rank, thread, hnbuf, clbuf);
#endif
  }

  MPI_Finalize();
  return(0);
}
