#!/bin/bash

# test1.89:
# fwd_map:  0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
# fwd_mask: 00000001,00000002,00000004,00000008,00000010,00000020,00000040,00000080,00000100,00000200,00000400,00000800,00001000,00002000,00004000,00008000

fwd_map=""
fwd_mask=""
cpu_cnt=0
task_cnt=15
# set task_cnt=15

for map_cpu in `seq 0 $task_cnt` ;do
        mask_cpu_tmp=$((1<<$map_cpu))  # = 2^(map_cpu)
        mask_cpu=`echo $mask_cpu_tmp |awk '{printf "%08x",$0}'`
        echo $map_cpu $mask_cpu_tmp $mask_cpu |awk '{printf "map_cpu=%2d => mask_cpu_tmp=%5d => mask_cpu=%s \n",$1,$2,$3}'
done

exit 0

./jg.sh
map_cpu= 0 => mask_cpu_tmp=    1 => mask_cpu=00000001
map_cpu= 1 => mask_cpu_tmp=    2 => mask_cpu=00000002
map_cpu= 2 => mask_cpu_tmp=    4 => mask_cpu=00000004
map_cpu= 3 => mask_cpu_tmp=    8 => mask_cpu=00000008
map_cpu= 4 => mask_cpu_tmp=   16 => mask_cpu=00000010
map_cpu= 5 => mask_cpu_tmp=   32 => mask_cpu=00000020
map_cpu= 6 => mask_cpu_tmp=   64 => mask_cpu=00000040
map_cpu= 7 => mask_cpu_tmp=  128 => mask_cpu=00000080
map_cpu= 8 => mask_cpu_tmp=  256 => mask_cpu=00000100
map_cpu= 9 => mask_cpu_tmp=  512 => mask_cpu=00000200
map_cpu=10 => mask_cpu_tmp= 1024 => mask_cpu=00000400
map_cpu=11 => mask_cpu_tmp= 2048 => mask_cpu=00000800
map_cpu=12 => mask_cpu_tmp= 4096 => mask_cpu=00001000
map_cpu=13 => mask_cpu_tmp= 8192 => mask_cpu=00002000
map_cpu=14 => mask_cpu_tmp=16384 => mask_cpu=00004000
map_cpu=15 => mask_cpu_tmp=32768 => mask_cpu=00008000

# srun --cpu_bind=map_cpu:0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
# srun --cpu_bind=mask_cpu:00000001,00000002,00000004,00000008,00000010,00000020,00000040,00000080,00000100,00000200,00000400,00000800,00001000,0 0002000,00004000,00008000
#  TASK_ID:0,MASK:1
#  TASK_ID:1,MASK:2
#  TASK_ID:2,MASK:4
#  TASK_ID:3,MASK:8
#  TASK_ID:4,MASK:16
#  TASK_ID:5,MASK:32
#  TASK_ID:6,MASK:64
#  TASK_ID:7,MASK:128
#  TASK_ID:8,MASK:256
#  TASK_ID:9,MASK:512
# TASK_ID:10,MASK:1024
# TASK_ID:11,MASK:2048
# TASK_ID:12,MASK:4096
# TASK_ID:13,MASK:8192
# TASK_ID:14,MASK:16384
# TASK_ID:15,MASK:32768



# It is strange that --cpu_bind=verbose (slurm/15.08.8) prints cpu bindings twice:
# export OMP_NUM_THREADS=1; srun --ntasks=2 --ntasks-per-node=2 --cpus-per-task=1 --ntasks-per-core=1 --cpu_bind=v,rank ./test.mpi.santis.intel15
        cpu_bind_cores=RANK - nid00035, task 0 0 [26262]: mask 0x1 set
        cpu_bind_cores=RANK - nid00035, task 0 0 [26262]: mask 0x1 set
        cpu_bind_cores=RANK - nid00035, task 1 1 [26263]: mask 0x2 set
        cpu_bind_cores=RANK - nid00035, task 1 1 [26263]: mask 0x2 set
        affinity test for 2 MPI ranks
        rank 0 @ nid00035 on cores [ 0 ]
        rank 1 @ nid00035 on cores [ 1 ]


srun -n1 -c4 --cpu_bind=mask_cpu:e
        thread 0 on cores [ 1 2 3 ]
        thread 1 on cores [ 1 2 3 ]
        thread 2 on cores [ 1 2 3 ]
        thread 3 on cores [ 1 2 3 ]
      "--cpu_bind=mask_cpu:e" 
means "use hexadecimal cpumask 0xe"
means "use cpumap 00001110"
means (from right to left):
        0,0,0,0,1,1,1,0 = cpumap
        7,6,5,4,3,2,1,0 = PU
=> maps only PU 1,2,3 => OK

# OK -------------------------------------------- ~/o/slurm/cpumask.ods & ~/o/hexa_binary_decimal_converter.sh
--cpu_bind=verbose,mask_cpu:0 => 00000000 = PU [ 0-72 ] = 0xffffffffffffffffff  
# hex=fffffffffffffff bin=1000000000000000057857959942726969827393378689175040438172647424
--cpu_bind=verbose,mask_cpu:1 => 00000001 = PU [ 0 ]
--cpu_bind=verbose,mask_cpu:2 => 00000010 = PU [ 1 ]
--cpu_bind=verbose,mask_cpu:3 => 00000011 = PU [ 0 1 ]
--cpu_bind=verbose,mask_cpu:4 => 00000100 = PU [ 2 ]
--cpu_bind=verbose,mask_cpu:5 => 00000101 = PU [ 0 2 ]
--cpu_bind=verbose,mask_cpu:6 => 00000110 = PU [ 1 2 ]
--cpu_bind=verbose,mask_cpu:7 => 00000111 = PU [ 0 1 2 ]
--cpu_bind=verbose,mask_cpu:8 => 00001000 = PU [ 3 ]
--cpu_bind=verbose,mask_cpu:9 => 00001001 = PU [ 0 3 ]
#
--cpu_bind=verbose,mask_cpu:a => 00001010 = PU [ 1 3 ]
--cpu_bind=verbose,mask_cpu:b => 00001011 = PU [ 0 1 3 ]
--cpu_bind=verbose,mask_cpu:c => 00001100 = PU [ 2 3 ]
--cpu_bind=verbose,mask_cpu:d => 00001101 = PU [ 0 2 3 ]
--cpu_bind=verbose,mask_cpu:e => 00001110 = PU [ 1 2 3 ]
--cpu_bind=verbose,mask_cpu:f => 00001111 = PU [ 0 1 2 3 ]
#
--cpu_bind=verbose,mask_cpu:10 => 00010000 = PU [ 4 ]
--cpu_bind=verbose,mask_cpu:11 => 00010001 = PU [ 0 4 ]
#
--cpu_bind=verbose,mask_cpu:aa
        ./hexa_binary_decimal_converter.sh b 10101010
        bin=10101010 dec=170
        bin=10101010 bin=10101010 pu=[ 1 3 5 7 ]
        bin=10101010 hex=0xAA
--cpu_bind=verbose,mask_cpu:bb
        ./hexa_binary_decimal_converter.sh h bb
        hex=bb dec=187
        hex=bb bin=10111011 pu=[ 0 1 3 4 5 7 ]
        hex=bb hex=0xbb
--cpu_bind=verbose,mask_cpu:cc
        ./hexa_binary_decimal_converter.sh h cc
        hex=cc dec=204
        hex=cc bin=11001100 pu=[ 2 3 6 7 ]
        hex=cc hex=0xcc
### bug for large number ?        
# --------------------------------------------
