#!/bin/bash

# docs.google.com/spreadsheets

in=$1

# --- success1:
#grep -q "^Done." $in ;rc=$?
grep -q 'End of program' $in ;rc=$?
if [ "$rc" != 0 ] ;then
    echo "in=$in Did job completed ? : rc=$rc != 0, exiting..."
    exit 0
#else
#    echo ok
fi


jobid=`grep SLURM_JOBID $in |awk '{print $4}'`
# --- success2:
sacct1=`sacct --noconvert --format=JobName,state -j$jobid |grep ChaNGa |awk '{print $2}'`
if [ "$sacct1" != "COMPLETED" ] ;then
    echo "sacct1=$sacct1 != COMPLETED, exiting..."
    exit 0
fi

# --- settings:
jobcn=`grep SLURM_JOB_NUM_NODES $in                     |awk '{print $4}'`
jobcputype=`grep SLURM_CPUS_ON_NODE $in                 |awk '{print $4}'` # 12 = haswell
jobnt=`grep "SLURM_NTASKS " $in                         |awk '{print $4}'`
jobntpn=`grep SLURM_NTASKS_PER_NODE $in                 |awk '{print $4}'`
jobcpt=`grep SLURM_CPUS_PER_TASK $in                    |awk '{print $4}'` # = omp
jobnpc=`grep SLURM_NTASKS_PER_CORE $in                  |awk '{print $4}'` # -j
jobcraycudamps=`grep ^CRAY_CUDA_MPS $in                 |cut -d= -f2`
if [ -z $jobcraycudamps ] ;then jobcraycudamps=notset ;fi
jobhugepagesize1=`grep ^HUGETLB_DEFAULT_PAGE_SIZE $in   |cut -d= -f2`
jobhugepagesize2=`grep 'Cray TLB page size' $in         |awk '{print $6}'`
jobhugetlb=`grep ^HUGETLB_MORECORE $in                  |cut -d= -f2`  # = no
jobchangaversion=`grep "^ChaNGa version" $in            |awk '{print $3}' |tr -d ","`
jobnp=`grep ^N: $in |awk '{print $2}'`

nexits=`grep '^EXIT HYBRID API' $in |wc -l`
#if [ $nexits -ne $jobcn ] ;then
#    echo "nexits=$nexits -ne jobcn=$jobcn, exiting..."
#    exit 0
#fi

# --- timings:
#t_changa=`grep '^ took ' $in |awk '{printf "%0.1f",$2}'`
#t_real=`grep '^real ' $in |awk '{printf "%0.1f",$2}'`
t_sacct=`sacct --noconvert --format=JobName,Elapsed -j$jobid |grep ChaNGa |awk '{print "~/linux.git/slurm/2seconds.sh "$2}' |sh |awk '{print $1}'`
#t_step1=`grep 'Step: 1.000000 Time:' $in |awk '{print $4}'`
#t_loadingp=`grep 'Loading particles' $in |awk '{printf "%0.1f",$8}'`

## big steps:
n_bigsteps=`grep "^Big step" $in |wc -l`
#t_bigstep=`grep "^Big step" $in |awk '{printf "%0.3f",$5}'`
t_bigsteps_sum=`grep "^Big step" $in |awk '{s=s+$5}END{printf "%0.3f",s}'`
t_bigsteps_min=`grep "^Big step" $in |awk '{printf "%0.3f\n",$5}' |sort -nk1 |head -1`
t_bigsteps_avg=`grep "^Big step" $in |echo $t_bigsteps_sum $n_bigsteps |awk '{printf "%0.3f",$1/$2}'`
t_bigsteps_max=`grep "^Big step" $in |awk '{printf "%0.3f\n",$5}' |sort -nk1 |tail -1`

t_kill=`grep "^KillAT" $in |awk '{printf "%0.3f",$4}'`

echo $in @ $jobcn @ $jobnt @ $jobntpn @ $jobcpt @ $jobnpc @ $t_sacct 

exit 0 

# --- results:
echo in=$in
echo jobchangaversion=$jobchangaversion
echo jobid=$jobid
echo jobcputype=$jobcputype
echo jobcn=$jobcn
echo nexits=$nexits
echo jobnt=$jobnt
echo jobntpn=$jobntpn
echo jobcpt=$jobcpt
echo jobnpc=$jobnpc
echo jobcraycudamps=$jobcraycudamps
echo jobhugepagesize1=$jobhugepagesize1
echo jobtlbpagesize2=$jobhugepagesize2
echo jobhugetlb=$jobhugetlb
echo jobnp=$jobnp
#echo "# ---"
#echo t_changa=$t_changa
#echo t_real=$t_real
#echo t_step1=$t_step1
#echo t_loadingp=$t_loadingp
echo     n_bigsteps=$n_bigsteps
echo t_bigsteps_sum=$t_bigsteps_sum
echo t_bigsteps_min=$t_bigsteps_min
echo t_bigsteps_avg=$t_bigsteps_avg
echo t_bigsteps_max=$t_bigsteps_max
echo t_kill=$t_kill
echo t_sacct=$t_sacct

exit 0

Running on Gemini (GNI) => Aries ?
