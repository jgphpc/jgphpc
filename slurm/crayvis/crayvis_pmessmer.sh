#!/bin/bash

# module load daint-gpu PyExtensions/3.6-CrayGNU-17.08

# in = nodelist of 1 job
# out = daint cabinets with colored compute nodes 

in=$1
out1=nid


# --- coordinates for the nids:
# xtprocadmin.daint
#  NID    (HEX)    NODENAME     TYPE    STATUS        MODE
#    1      0x1  c0-0c0s0n1  service        up       batch
#    2      0x2  c0-0c0s0n2  service        up       batch
#    4      0x4  c0-0c0s1n0  compute        up       batch
#    5      0x5  c0-0c0s1n1  compute        up       batch
#   ...
if [ ! -e xtprocadmin.daint ] ;then
    xtprocadmin > xtprocadmin.daint
fi

# --- list of nids:
nodelist=`grep SLURM_JOB_NODELIST $in |cut -d= -f2`
echo $nodelist
hostlist -e $nodelist |awk -Fnid '{print $2}' > nid
# hostlist -e `sacct -j $jid -o nodelist -P |grep -m1 ^nid` |awk -Fnid '{print $2}' > eff.nid

# --- cn:
cn=`wc -l nid |awk '{print $1}'`
#cn=`grep SLURM_NNODES $in |awk '{print $4}'`

python3 ./crayvis_pmessmer.py xtprocadmin.daint $out1 ${cn}cn.png
echo "eog ${cn}.png"

