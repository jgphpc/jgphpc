#!/bin/sh

# http://unix.stackexchange.com/questions/33450/checking-if-hyperthreading-is-enabled-or-not/33509#33509
# If the number of logical processors is twice the number of cores you have HT:
# santis: nid00012: 1 physical CPU(s) / 8 cores per physical CPU / 16 logical CPU(s) / HT is ON
#  brisi: nid00035: 2 physical CPU(s) / 12 cores per physical CPU / 48 logical CPU(s) / HT is ON
#   dora: nid00847: 2 physical CPU(s) / 12 cores per physical CPU / 48 logical CPU(s) / HT is ON
#  daint: nid03977: 1 physical CPU(s) / 8 cores per physical CPU / 16 logical CPU(s) / HT is ON
#        pilatus11: 2 physical CPU(s) / 8 cores per physical CPU / 32 logical CPU(s) / HT is ON
# h-express   leone39: 2 physical CPU(s) / 8 cores per physical CPU / 16 logical CPU(s) / HT is OFF
# interactive leone31: 2 physical CPU(s) / 12 cores per physical CPU / 24 logical CPU(s) / HT is OFF
#        keschcn-0001: 2 physical CPU(s) / 12 cores per physical CPU / 24 logical CPU(s) / HT is OFF
# todo: comparer avec scontrol show config |grep MaxTasksPerNode

# -----------------------------------------------------------------------------------
CPUFILE=/proc/cpuinfo
# SR="srun -n1 -t1"
NUMPHY=`grep "physical id" $CPUFILE | sort -u |wc -l`
NUMCORE=`grep "core id" $CPUFILE |sort -u |wc -l`
NUMLOG=`grep "processor" $CPUFILE |wc -l`
H=`uname -n`
NUMPHY_NUMCORE=$((NUMPHY*NUMCORE))
HT=`echo $NUMLOG $NUMPHY_NUMCORE |awk '{print $1/$2}'`

# -----------------------------------------------------------------------------------
DefMemPerNode=`scontrol show config |grep DefMemPerNode |cut -d= -f2 |tr -d " "`
MaxMemPerNode=`scontrol show config |grep MaxMemPerNode |cut -d= -f2 |tr -d " "`
DefaultMemPerCPU_MB=`scontrol show config |grep DefMemPerCPU|cut -d= -f2 |tr -d " "` 
MemTotal_MB=`grep MemTotal /proc/meminfo |awk '{print $2/1024}' `
IdealMemPerCPU_MB=`echo $MemTotal_MB $NUMLOG |awk '{printf "%d",$1/$2}'`
# if [ "$DefaultMemPerCPU_MB" -ne "$IdealMemPerCPU_MB" ] ; then
# memres=`echo "DefaultMemPerCPU_MB=$DefaultMemPerCPU_MB IdealMemPerCPU_MB=$IdealMemPerCPU_MB"`
memres=`echo "DftMpC=$DefaultMemPerCPU_MB IdealMpC=$IdealMemPerCPU_MB DftMpN=$DefMemPerNode MMpN=$MaxMemPerNode"`
#  fi
h=$HOST
# -----------------------------------------------------------------------------------
if [ "$HT" -eq 2 ] ;then
        echo "$H: $NUMPHY physicalCPU(s) / $NUMCORE cores per physical CPU / $NUMLOG logicalCPU(s) / HT is ON / $memres $h"
else
        echo "$H: $NUMPHY physicalCPU(s) / $NUMCORE cores per physical CPU / $NUMLOG logicalCPU(s) / HT is OFF / $memres $h"
        # per physical CPU
fi

exit 0

# -------
# memory:
scontrol show config |egrep "DefMemPerCPU|MaxMemPerCPU|DefMemPerNode|MaxMemPerNode"
# grep MemTotal /proc/meminfo # MemTotal:       32991184 kB
nid00012: 1 physicalCPU(s) / 8 cores per physical CPU / 16 logicalCPU(s) / HT is ON / DftMpC=1337 IdealMpC=2013 DftMpN= MMpN= santis01
nid00173: 1 physicalCPU(s) / 8 cores per physical CPU / 16 logicalCPU(s) / HT is ON / DftMpC= IdealMpC=2013 DftMpN=32768 MMpN=32768 daint01
nid00035: 2 physicalCPU(s) / 12 cores per physical CPU / 48 logicalCPU(s) / HT is ON / DftMpC=1337 IdealMpC=1342 DftMpN= MMpN= brisi01
nid00077: 2 physicalCPU(s) / 12 cores per physical CPU / 48 logicalCPU(s) / HT is ON / DftMpC= IdealMpC=1342 DftMpN=65536 MMpN=65536 dora01
pilatus03: 2 physicalCPU(s) / 8 cores per physical CPU / 32 logicalCPU(s) / HT is ON / DftMpC= IdealMpC=2015 DftMpN=64000 MMpN=UNLIMITED
leone39: 2 physicalCPU(s) / 8 cores per physical CPU / 16 logicalCPU(s) / HT is OFF / DftMpC= IdealMpC=16147 DftMpN=UNLIMITED MMpN=UNLIMITED
keschcn-0001: 2 physicalCPU(s) / 12 cores per physical CPU / 24 logicalCPU(s) / HT is OFF / DftMpC= IdealMpC=10765 DftMpN=UNLIMITED MMpN=UNLIMITED

# -------
# echo -n The CPU is a `grep "model name" $CPUFILE | sort -u | cut -d : -f 2-`
# echo " with`grep "cache size" $CPUFILE | sort -u | cut -d : -f 2-` cache"
