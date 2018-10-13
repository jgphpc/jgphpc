#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <mpi.h>
#ifdef _OPENMP
#include <omp.h>
#endif

#include <time.h>
#include <sys/time.h>

void print_current_time(void) {

    struct timeval currentt;
    // printf("usec1=%d\n",currentt.tv_usec);
    time_t t = time(NULL);
    struct tm tm;

    tm = *localtime(&t);
    gettimeofday(&currentt,NULL);
    printf("t: %04d-%02d-%02d %02d:%02d:%02d:%d\n", \
    tm.tm_year + 1900, \
    tm.tm_mon + 1, \
    tm.tm_mday, \
    tm.tm_hour, tm.tm_min, tm.tm_sec, \
    currentt.tv_usec);

/*
    gettimeofday(&endt,NULL);
    printf("usec2=%d\n",endt.tv_usec);
    int elapsed = ((endt.tv_sec - startt.tv_sec) * 1000000) + (endt.tv_usec - startt.tv_usec);
    printf("elapsed=%d microseconds\n",elapsed);
*/

}

void print_openacc_version(void) {
    // module load craype-accel-nvidia60
    int cscs_oacc_v;

#ifdef _OPENACC
    switch (_OPENACC) {
        case 201111: cscs_oacc_v=10201111; break;
        case 201306: cscs_oacc_v=20201306; break;
        case 201510: cscs_oacc_v=25201510; break;
        default:     cscs_oacc_v=_OPENMP;
    }
    printf("oaccv=%d \n", cscs_oacc_v);
#else
    printf("oaccv=no \n");
#endif 

}

void print_openmp_version(void) {

    int cscs_omp_v; // , ompnumthreadid, ompnumthreads1;
    // char* ompnumthreads2 = getenv ("OMP_NUM_THREADS");

#ifdef _OPENMP
    switch (_OPENMP) {
        case 200805: cscs_omp_v=30200805; break;
        case 201107: cscs_omp_v=31201107; break;
        case 201307: cscs_omp_v=40201307; break;
        case 201511: cscs_omp_v=45201511; break;
        default:     cscs_omp_v=_OPENMP;
    }
    printf("ompv=%d \n", cscs_omp_v);
    // printf("ompv=%d OMP_NUM_THREADS=%s\n", cscs_omp_v, ompnumthreads2);
#else
    printf("ompv=no \n");
    
#endif

/*
    #pragma omp parallel private(ompnumthreadid) shared(ompnumthreads1)
    {
        ompnumthreadid = omp_get_thread_num();
        // #pragma omp barrier
        #pragma omp master
        {
            ompnumthreads1 = omp_get_num_threads();
            std::cout << "OPENMP version: " << cscs_omp_v
                      << " num_threads=" << ompnumthreads1
                      << " OMP_NUM_THREADS=" << ompnumthreads2
                      << std::endl; 
        }
    }
*/

}

void print_mpi_version(void) {

// http://trac.mpich.org/projects/mpich/roadmap?show=completed
// 201304 304
// 201402 310
// 201406 311
// 201407 312
// 201410 313
// 201511 320
// 201602 321
// 201605 322
// 201608 323
// 201705 330

    // export MPICH_VERSION_DISPLAY=1
    int cscs_mpi_v=0, cscs_mpi_subv=0;
    char cscs_mpi_vv[MPI_MAX_LIBRARY_VERSION_STRING];
    int reslen=-1;
    MPI_Get_version( &cscs_mpi_v, &cscs_mpi_subv );
    MPI_Get_library_version(cscs_mpi_vv, &reslen);
    printf("mpiv=%.*s", 59, cscs_mpi_vv);
    printf(" / %d.%d \n", cscs_mpi_v, cscs_mpi_subv);

}

void print_proc_stat(int rank) {

    // TODO: getenv(SLURM_PROCID)
    int size=-1, len=-1;
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    char namecn[MPI_MAX_PROCESSOR_NAME];
    MPI_Get_processor_name(namecn, &len);

    // Get the the current process' stat file from the /proc filesystem
    // man proc => Status information about the process
    FILE* procfile = fopen("/proc/self/stat", "r");
    long to_read = 8192;
    char buffer[to_read];
    int read = fread(buffer, sizeof(char), to_read, procfile);
    fclose(procfile);

    // Field with index 38 (zero-based counting) is what we want (processor)
    char* line = strtok(buffer, " ");
    int i;
    for (i = 1; i < 38; i++)
    {
        line = strtok(NULL, " ");
    }

    line = strtok(NULL, " ");
    int cpu_id = atoi(line);
    printf("rank:%04d/%04d nid=%s cpuid=%d\n", rank, size, namecn, cpu_id);

    //int rank = atoi(getenv("SLURM_PROCID"));
    //printf("rank: %d, cpuid: %d\n", rank, cpu_id);

    // man proc => Status information about the process
	//1             pid %d      The process ID.
	//2             comm %s     The filename  of  the  executable,  in  parentheses.
	//3             state %c    One character from the string "RSDZTW"  where  R  is
	//4             ppid %d     The PID of the parent.
	//5             pgrp %d     The process group ID of the process.
	//6             session %d  The session ID of the process.
	//7             tty_nr %d   The controlling terminal of the process.  (The minor
	//8             tpgid %d    The  ID  of the foreground process group of the con-
	//9             flags %u (%lu before Linux 2.6.22)
	//10            minflt %lu  The number of minor  faults  the  process  has  made
	//11            cminflt %lu The  number  of  minor  faults  that  the  process's
	//12            majflt %lu  The  number  of  major  faults  the process has made
	//13            cmajflt %lu The  number  of  major  faults  that  the  process's
	//14            utime %lu   Amount of time that this process has been  scheduled
	//15            stime %lu   Amount of time that this process has been  scheduled
	//16            cutime %ld  Amount of time that this process's waited-for  chil-
	//17            cstime %ld  Amount  of time that this process's waited-for chil-
	//18            priority %ld
	//19            nice %ld    The nice value (see setpriority(2)), a value in  the
	//20            num_threads %ld
	//21            itrealvalue %ld
	//22            starttime %llu (was %lu before Linux 2.6)
	//23            vsize %lu   Virtual memory size in bytes.
	//24            rss %ld     Resident  Set  Size: number of pages the process has
	//25            rsslim %lu  Current  soft  limit in bytes on the rss of the pro-
	//26            startcode %lu
	//27            endcode %lu The address below which program text can run.
	//28            startstack %lu
	//29            kstkesp %lu The current value of ESP (stack pointer),  as  found
	//30            kstkeip %lu The current EIP (instruction pointer).
	//31            signal %lu  The  bitmap of pending signals, displayed as a deci-
	//32            blocked %lu The bitmap of blocked signals, displayed as a  deci-
	//33            sigignore %lu
	//34            sigcatch %lu
	//35            wchan %lu   This  is the "channel" in which the process is wait-
	//36            nswap %lu   Number of pages swapped (not maintained).
	//37            cnswap %lu  Cumulative  nswap  for  child  processes  (not main-
	//38            exit_signal %d (since Linux 2.1.22)
	//39            processor %d (since Linux 2.2.8)
	//40            rt_priority %u (since Linux 2.5.19; was %lu before Linux 2.6.22)
	//41            policy %u (since Linux 2.5.19; was %lu before Linux 2.6.22)
	//42            delayacct_blkio_ticks %llu (since Linux 2.6.18)
	//43            guest_time %lu (since Linux 2.6.24)
	//44            cguest_time %ld (since Linux 2.6.24)
	//
}

// man date_and_time (cce/ftn)
//  values(1) YYYY
//  values(2) MM
//  values(3) DD
//  values(4) The time difference, in minutes, with respect to UTC, or -HUGE (0)
//  values(5) HH
//  values(6) MM
//  values(7) SS
//  values(8) ms


int main( int argc, char *argv[] )
{
    int rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank==0) {
    print_current_time();
    print_mpi_version();
    print_openmp_version();
    print_openacc_version();
    }

    MPI_Barrier(MPI_COMM_WORLD);
    print_proc_stat(rank);

    if (rank==0) print_current_time();

    MPI_Finalize();
    return 0;
}


