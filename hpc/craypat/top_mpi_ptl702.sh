#!/bin/bash

# --- ptl/7.0.2
# CrayPat/X:  Version 7.0.2 Revision a975333  05/16/18 15:54:03
# Experiment:                  lite  lite/sample_profile
# Number of PEs (MPI ranks):    384
# Numbers of PEs per Node:       12  PEs on each of  32  Nodes
# Numbers of Threads per PE:      2
# Number of Cores per Socket:    12
# Execution start time:  Tue Oct 23 15:05:46 2018
# System name and speed:  nid02215  2.601 GHz (nominal)
# Intel Haswell    CPU  Family:  6  Model: 63  Stepping:  2
# DRAM:  64 GiB DDR4-2400 on 2.6 GHz nodes
# DRAM:  64 GiB DDR4-2133 on 2.6 GHz nodes  for 432 PEs
# 
# 
# Avg Process Time:             1,419 secs
# High Memory:               89,609.8 MiBytes     233.4 MiBytes per PE
# Observed CPU clock boost:     113.9 %
# Percent cycles stalled:        42.0 %
# Instr per Cycle:               0.66
# I/O Read Rate:            15.413575 MiBytes/sec
# I/O Write Rate:            0.212672 MiBytes/sec
# 
# Table 1:  Profile by Function
# 
#   Samp% |      Samp |     Imb. |  Imb. | Group
#         |           |     Samp | Samp% |  Function=[MAX10]
#         |           |          |       |   PE=HIDE
#         |           |          |       |    Thread=HIDE
#        
#  100.0% | 139,965.0 |       -- |    -- | Total
# |----------------------------------------------------------------------------
# |  95.9% | 134,265.3 |       -- |    -- | ETC
# ||---------------------------------------------------------------------------
# ||  52.3% |  73,235.2 | 16,406.8 | 18.4% | GOMP_parallel
# ||  15.0% |  21,036.5 |  4,813.5 | 18.7% | hypre_ParCSRSubspacePrec
# ||  10.4% |  14,545.0 | 20,459.0 | 58.6% | hypre_ParCSRPersistentCommHandleWait
# ||   5.3% |   7,369.7 |  6,234.3 | 45.9% | VecAssemblyBegin_MPI
# ||   4.6% |   6,407.8 | 10,267.2 | 61.7% | hypre_ParCSRCommHandleDestroy
# ||   1.4% |   1,895.5 |  1,788.5 | 48.7% | hypre_ParVectorInnerProd
# ||   1.2% |   1,693.8 |    414.2 | 19.7% | hypre_CSRMatrixMatvecT._omp_fn.10
# ||   1.1% |   1,604.6 |  1,090.4 | 40.6% | gomp_team_barrier_wait_end
# ||   1.0% |   1,363.9 |  1,301.1 | 48.9% | hypre_ParCSRCommHandleCreate
# ||===========================================================================
# |   2.4% |   3,403.1 |       -- |    -- | MPI
# ||---------------------------------------------------------------------------
# ||   1.2% |   1,610.3 |  1,256.7 | 43.9% | MPI_Allreduce
# ||===========================================================================
# |   1.1% |   1,603.7 |       -- |    -- | USER
# |============================================================================

in=$1  # in=xf.txt
dos2unix $in &> /dev/null
t1=$2  # speedup=t1/tn
c1=$3  # idealspeedup=cn/c1

# 
title='Table 1:  Profile by Function'
#title='Table 1:  Profile by Function Group and Function'
#tn=`grep -50 "$title" $in |grep \|Total |cut -d \| -f1 |tr -d " "`

craypatv=`grep 'CrayPat/X' $in |awk '{print $3}'`
mppwidth=`grep -m1 'Number of PEs ' $in |awk -F: '{print $2}'|tr -d " "`

userper=`   grep -50 "$title" $in |grep -m1 "| USER"            |cut -d \| -f2 |tr -d " "`
mpicommper=`grep -50 "$title" $in |grep "| MPI$"            |cut -d \| -f2 |tr -d " "`
mpiA=`      grep -50 "$title" $in |grep -A2 "| MPI$"|tail -1|cut -d \| -f3 |tr -d " "`
mpiB=`      grep -50 "$title" $in |grep -A3 "| MPI$"|tail -1|cut -d \| -f3 |tr -d " "`
mpiC=`      grep -50 "$title" $in |grep -A4 "| MPI$"|tail -1|cut -d \| -f3 |tr -d " "`
#mpiD=`      grep -50 "$title" $in |grep -A5 "|MPI$"|tail -1|cut -d \| -f3 |tr -d " "`
echo $in craypatv=$craypatv mppwidth=$mppwidth
echo user%=$userper mpi%=$mpicommper mpiA=$mpiA mpiB=$mpiB mpiC=$mpiC $mppwidth
#echo $in @$userper @ $mpicommper @$mpiA @$mpiB @$mpiC @$mpiD |tr -d " "|tr -d "%"
mpicallA=`  grep -50 "$title" $in |grep -A2 "| MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
mpicallB=`  grep -50 "$title" $in |grep -A3 "| MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
mpicallC=`  grep -50 "$title" $in |grep -A4 "| MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
#mpicallD=`  grep -50 "$title" $in |grep -A5 "|MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
echo mpicallA=$mpicallA mpicallB=$mpicallB mpicallC=$mpicallC
#echo $in @$userper @ $mpicommper @$mpicallA @$mpicallB @$mpicallC @$mpicallD |tr -d " "|tr -d "%"
echo
exit 0
#speedup=`echo $t1 $tn |awk '{print $1/$2}'`
#thspeedup=`echo $mppwidth $c1 |awk '{print $1/$2}'`
#userper=`grep -50 "$title" $in |grep \|USER |cut -d \| -f2 |tr -d " "`
#mpisyncper=`grep -50 "$title" $in |grep \|MPI_SYNC |cut -d \| -f2 |tr -d " "`
#mpicommper=`grep -50 "$title" $in |grep "|MPI$" |cut -d \| -f2 |tr -d " "`
#mpiper=`echo $mpisyncper $mpicommper |awk '{print $1+$2"%"}'`
#etcper=`grep -50 "$title" $in |grep "|ETC$" |cut -d \| -f2 |tr -d " "`
#echo $mppwidth @ $speedup @ $thspeedup @ $tn @ $userper @ $mpiper @ $mpicommper @ $mpisyncper @ $etcper @ $mppnppn @ $mppdepth @ $cn @ $cpersocket | tr -d " " | tr -d %
