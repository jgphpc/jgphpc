#!/bin/bash

in=$1
# ~jenscscs/rt30378/o_5605747 0M
# ~jenscscs/rt30378/o_5605748 2M

# --- snx3000 | snx1600
snx=`grep pwd= $in |cut -d/ -f3`

# --- gpu | mc ?
# gpu_mc=`grep cdo $in |cut -d/ -f7`

# --- cdo version
cdo=`grep "bin/cdo" $in`

# --- hugep
hugep=`grep HUGETLB_DEFAULT_PAGE_SIZE= $in |cut -d= -f2`
if [ -z $hugep ] ; then hugep=0M ;fi

# --- reals
reals=`grep ^real $in |wc -l`
if [ $reals -ne 3 ] ;then 
    #echo "reals=$reals/=3 !!! $in" 
    exit 0
else
    m1=`grep -m1 ^real $in |awk '{print $2}'`
    m2=`grep -m2 ^real $in |awk '{print $2}' |tail -1`
    m3=`grep -m3 ^real $in |awk '{print $2}' |tail -1`
fi

jid=`echo $in|cut -d_ -f2`
submit=`SLURM_TIME_FORMAT=%Y/%m/%d-%H:%M:%S sacct -j $jid --format=jobid,submit,start,end |grep ^$jid |head -1 |awk '{print $2}'`
start=`SLURM_TIME_FORMAT=%Y/%m/%d-%H:%M:%S sacct -j $jid --format=jobid,submit,start,end |grep ^$jid |head -1 |awk '{print $3}'`
end=`SLURM_TIME_FORMAT=%Y/%m/%d-%H:%M:%S sacct -j $jid --format=jobid,submit,start,end |grep ^$jid |head -1 |awk '{print $4}'`

echo $cdo $hugep $m1 $m2 $m3 $in $jid $submit $start $end $snx
# echo $gpu_mc $hugep $m1 $m2 $m3 $in $jid $submit $start $end $snx
