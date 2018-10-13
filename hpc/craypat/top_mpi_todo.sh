#!/bin/bash

# --- ptl/6.5.2

in=$1  # in=xf.txt
dos2unix $in &> /dev/null
t1=$2  # speedup=t1/tn
c1=$3  # idealspeedup=cn/c1

# Table 1:  Profile by Function
# 
#  Samp % |  Samp |Imb. Samp |   Imb. |Experiment=1
#         |       |          | Samp % |Group
#         |       |          |        | Function
#         |       |          |        |  PE='HIDE'
# 
#  100.0% | 38899 |       -- |     -- |Total
# |------------------------------------------------
# |  53.7% | 20894 |       -- |     -- |USER
# ||-----------------------------------------------
# ||  19.2% |  7479 |  1549.37 |  17.2% |fast_waves_rk_fast_waves_runge_kutta_
# ||   3.9% |  1533 |   244.18 |  13.8% |src_slow_tendencies_rk_complete_tendencies_uvwtpp_
# ||===============================================
# |  33.0% | 12853 |       -- |     -- |MPI
# ||-----------------------------------------------
# ||  13.2% |  5133 | 29404.49 |  85.3% |mpi_recv
# ||   5.4% |  2117 |  1596.28 |  43.1% |MPI_ALLREDUCE
# ||===============================================
# 
title='Table 1:  Profile by Function'
#title='Table 1:  Profile by Function Group and Function'
#tn=`grep -50 "$title" $in |grep \|Total |cut -d \| -f1 |tr -d " "`

craypatv=`grep 'CrayPat/X' $in |awk '{print $3}'`
mppwidth=`grep 'Number of PEs ' $in |awk -F: '{print $2}'|tr -d " "`

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
