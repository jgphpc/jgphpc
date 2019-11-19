#!/bin/bash

# If cmd return O then is in exclusive mode and we can proceed with resetting the cache 
# 
cmd=$(scontrol show job ${SLURM_JOB_ID} -o | awk 'match($0,/Shared=\w+/) {print substr($0,RSTART,RLENGTH)}' | awk -F'=' '{print $2}')

if [ $cmd -eq 0 ] ; then
	logger "Node ${SLURMD_NODENAME} is in exclusive mode, I will drop the cache"
	echo 1 > /proc/sys/vm/drop_caches
fi

# kernel parameter: (vm.zone_reclaim_mode = 0)

exit 0

