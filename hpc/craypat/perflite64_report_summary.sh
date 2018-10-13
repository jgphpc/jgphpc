#!/bin/bash

in=$1   # *.rpt
# dos2unix $in 
#in=$1  # in=xf.txt
#t1=$2  # speedup=t1/tn
#c1=$3  # idealspeedup=cn/c1

# ------------------------------------------------------------------
# CrayPat/X:  Version 6.4.2 Revision 240cf5a  08/22/16 15:52:17
# Experiment:                  lite  lite/sample_profile
# Number of PEs (MPI ranks):     64
# Numbers of PEs per Node:        8  PEs on each of  8  Nodes
# Numbers of Threads per PE:      1
# Number of Cores per Socket:     8
# Execution start time:  Mon Dec 26 16:41:54 2016
# System name and speed:  nid00008  2601 MHz (approx)
# Intel sandybridge CPU  Family:  6  Model: 45  Stepping:  7
# Avg Process Time:      473.83 secs
# High Memory:         21,647.0 MBytes      338.2 MBytes per PE
# MFLOPS (aggregate): 45,821.01 M/sec      715.95 M/sec per PE
# I/O Read Rate:      25.663687 MBytes/sec
# I/O Write Rate:     10.990694 MBytes/sec
# Avg CPU Energy:       499,847 joules     62,481 joules per node
# Avg CPU Power:          1,055 watts      131.86 watts per node
# Avg ACC Energy:        40,785 joules      5,098 joules per node
# Avg ACC Power:          86.08 watts       10.76 watts per node
# ------------------------------------------------------------------

craypatv=`grep 'CrayPat/X' $in |awk '{print $3}'`
mppwidth=`grep 'Number of PEs ' $in |awk -F: '{print $2}'|tr -d " "`
mppnppn=`grep -A1 'Numbers of PEs per Node:' $in |tail -1|awk '{print $6}'`
cn=`grep 'Numbers of PEs per Node:' $in |awk '{print $11}'`
if [ -z $cn ] ;then cn=1 ;fi
mppdepth=`grep 'Numbers of Threads per PE:' $in |awk '{print $6}'`
cpersocket=`grep 'Number of Cores per Socket:' $in |awk -F: '{print $2}'|tr -d " "`
cputype=`grep -A1 "^System name" $in |tail -1`
memoryMBytes=`grep "^High Memory:" $in |awk '{print $3}' |tr -d \, |awk '{printf "%.0f", $0}'`
memoryMBytesperPE=`grep "^High Memory:" $in |awk '{printf "%.0f", $5}'`

echo "xpat/$craypatv @ c=$mppwidth @ omp=$mppdepth @ ppn=$mppnppn @ cn=$cn @ cpers=$cpersocket"
echo "cputype=$cputype"
echo "memory=${memoryMBytes}MB @ memoryperPE=${memoryMBytesperPE}MB @ c=$mppwidth"

# exit 0

# Table 1:  Profile by Function Group and Function (top 10 functions shown)
# 
#   Samp% |     Samp |    Imb. |  Imb. |Group
#         |          |    Samp | Samp% | Function
#         |          |         |       |  PE=HIDE
# 
#  100.0% | 46,712.1 |      -- |    -- |Total
# |-----------------------------------------------------------------------------
# |  60.6% | 28,311.0 |      -- |    -- |MPI
# ||----------------------------------------------------------------------------
# ||  57.4% | 26,792.0 | 8,393.0 | 24.2% |MPI_ALLREDUCE
# ||============================================================================
# |  36.3% | 16,972.0 |      -- |    -- |USER
# ||----------------------------------------------------------------------------
# ||   4.5% |  2,121.1 | 6,346.9 | 76.1% |fluxintegration_mod_mp_fluxintegration_

title='Table 1:  Profile by Function Group'
tn=`grep -50 "$title" $in |grep \|Total |head -1 |cut -d \| -f1 |tr -d " "`
tsamples=`grep -50 "$title" $in |grep \|Total |head -1 |cut -d \| -f2 |tr -d " " |tr -d \,`
userper=`grep -50 "$title" $in |grep \|USER |cut -d \| -f2 |tr -d " "`
mpisyncper=`grep -50 "$title" $in |grep \|MPI_SYNC |cut -d \| -f2 |tr -d " "`
if [ -z $mpisyncper ] ;then mpisyncper=0 ;fi
mpicommper=`grep -50 "$title" $in |grep "|MPI$" |cut -d \| -f2 |tr -d " "`
mpiper=`echo $mpisyncper $mpicommper |awk '{print $1+$2"%"}'`
etcper=`grep -50 "$title" $in |grep "|ETC$" |cut -d \| -f2 |tr -d " "`

echo in=$in
echo c=$mppwidth @ total=$tn @ user=$userper @ mpi=$mpiper @ mpicomm=$mpicommper @ mpisync=$mpisyncper @ etc=$etcper
echo "# $mppwidth @ $tn @ $userper @ $mpiper @ $mpicommper @ $mpisyncper @ $etcper @ $mppnppn @ $mppdepth @ $cn @ $cpersocket" | tr -d " " | tr -d %

#   Table 3:  File Input Stats by Filename
# 
#        Read |  Read MBytes |  Read Rate |     Reads |   Bytes/ |File Name[max10]
#        Time |              | MBytes/sec |           |     Call | PE=HIDE
# 
#    8.397388 | 6,495.387688 | 773.500976 | 854,593.0 | 7,969.77 |Total
#   |-----------------------------------------------------------------------------
#   | 8.222048 | 6,483.560669 | 788.557905 | 831,936.0 | 8,171.91 |/scratch/snx2000/piccinal/perftools/santis01/0.00126141/memory-16c-2cpcn-08cn/0.00126141/AEEP_Test_clr11-12_racleur.stl  | 0.155537 |    10.220276 |  65.709801 |   4,384.0 | 2,444.51 |/scratch/snx2000/piccinal/perftools/santis01/0.00126141/memory-16c-2cpcn-08cn/0.00126141/namelist.xml
#   | 0.019754 |     1.605942 |  81.298162 |  18,168.0 |    92.69 |/proc/self/maps
#   | 0.000050 |     0.000801 |  16.051906 |     105.0 |     8.00 |_UnknownFile_
#   |=============================================================================
avgtimesec=`grep "^Avg Process Time:" $in |awk '{print $4}' |tr -d \,`
readtime=`grep -A6 'Table 3:  File Input Stats by Filename' $in |grep \|Total |cut -d \| -f1 |tr -d " " |tr -d \, |awk '{printf "%.0f",$0}'`
readtimeper=`echo $readtime $tsamples |awk '{printf "%.1f" ,$1/$2*100}'`
echo "ioreadtime=$readtime samples @readtimeper=$readtimeper%"

# 
#   Table 4:  File Output Stats by Filename
# 
#    Write Time |     Write | Write Rate |   Writes |     Bytes/ |File Name[max10]
#               |    MBytes | MBytes/sec |          |       Call | PE=HIDE
# 
#    233.208412 | 95.626715 |   0.410048 | 26,073.0 |   3,845.81 |Total
#   |-----------------------------------------------------------------------------
#   | 233.195615 | 94.858437 |   0.406776 |    922.0 | 107,881.00 |flow0.h5
#   |   0.011976 |  0.765656 |  63.932796 | 25,089.0 |      32.00 |_UnknownFile_
#   |   0.000821 |  0.002623 |   3.195815 |     62.0 |      44.35 |stdout
#   |=============================================================================
writetime=`grep -A6 'Table 4:  File Output Stats by Filename' $in |grep \|Total |cut -d \| -f1 |tr -d " " |tr -d \, |awk '{printf "%.0f",$0}'`
writetimeper=`echo $writetime $tsamples |awk '{printf "%.1f" ,$1/$2*100}'`
#echo "iowritetime=$writetime samples @writetimeper=$writetimeper% @tsamples=$tsamples @elapsedtime=$avgtimesec sec"
echo "iowritetime=$writetime/$tsamples samples ($writetimeper%) @c= $mppwidth @elapsedtime=$avgtimesec sec"

