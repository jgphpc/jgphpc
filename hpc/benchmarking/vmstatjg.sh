#!/bin/sh

# see https://github.com/eth-cscs/reframe/pull/1613/files

# USAGE :  vmstatjg.sh ; /usr/bin/vmstat -S M
# reference : procps/vmstat.c
# vmstat -S 
# k : kilo_bits
# K : kilo_OCTETS
# m : mega_bits
# M : mega_OCTETS

# If only needs a single core but more
# than 2000mb of memory they need to specify how much memory they want slurm to
# allocate in their submission.
# 
# scontrol show config | grep -i mem
# DefMemPerCPU = 2000
# MaxMemPerNode = UNLIMITED
# SelectTypeParameters = CR_CPU_MEMORY,CR_LLN
# 
# Could you try to define the memory per node in the batch script?
# #SBATCH --mem=48g
# or even choose nodes with large memory:
# #SBATCH --partition=largeMem

function affiche_swapMb {
	echo $1 $2 | awk '{print "kb_swap_total - kb_swap_free = kb_swap_used (Mbits) : ",($1-$2)/1000000*1024}'
}
function affiche_swapMo {
	echo $1 $2 | awk '{print "kb_swap_total - kb_swap_free = kb_swap_used (Mo)    : ",($1-$2)/1024}'
}

function affiche_memMb {
	echo $1 $2 | awk '{print "kb_memory_total - kb_memory_free = kb_memory_used (Mbits) : ",($1-$2)/1000000*1024}'
}
function affiche_memMo {
	echo $1 $2 | awk '{print "kb_memory_total - kb_memory_free = kb_memory_used (Mo)    : ",($1-$2)/1024}'
}

function affiche_ {
	echo "total  used  free --- total  used  free (Mo)"
	echo $1 $2 $3 $4 | awk '{printf "%5.0f %5.0f %5.0f --- %5.0f %5.0f %5.0f\n", $1/1024,($1-$2)/1024,$2/1024,$3/1024,($3-$4)/1024,$4/1024}'
###	echo $1 $2 $3 $4 | awk '{printf "%5.0f %5.0f %5.0f --- %5.0f %5.0f %5.0f\n", $1/1000000*1024,($1-$2)/1000000*1024,$2/1000000*1024,$3/1000000*1024,($3-$4)/1000000*1024,$4/1000000*1024}'
###	echo "total  used  free --- total  used  free (Mbits)"
}


kb_swap_total=`grep SwapTotal /proc/meminfo | awk '{print $2}'`
kb_swap_free=` grep SwapFree  /proc/meminfo | awk '{print $2}'`
###affiche_swapMb $kb_swap_total $kb_swap_free 
###affiche_swapMo $kb_swap_total $kb_swap_free 
#
kb_main_total=`grep MemTotal /proc/meminfo | awk '{print $2}'`
kb_main_free=` grep MemFree  /proc/meminfo | awk '{print $2}'`
###affiche_memMb $kb_main_total $kb_main_free 
###affiche_memMo $kb_main_total $kb_main_free 
affiche_ $kb_main_total $kb_main_free $kb_swap_total $kb_swap_free
