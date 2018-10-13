#!/bin/bash

# --- perftools-lite/6.5.2

in=$1  # in=xf.txt
dos2unix $in &> /dev/null

# Table 1:  Profile by Function
# 
#   Samp% |     Samp |  Imb. |  Imb. | Group
#         |          |  Samp | Samp% |  Function=[MAX10]
#         |          |       |       |   PE=HIDE
# 
#  100.0% | 22,270.0 |    -- |    -- | Total
# |-----------------------------------------------------------------------------
# |  92.0% | 20,481.5 |    -- |    -- | USER
# ||----------------------------------------------------------------------------
# ||  37.0% |  8,236.3 | 153.7 |  2.0% | tvr_fluid_fluid$interaction_tvr_fluid$interaction_tvr_fluid_mod_
# ||  18.8% |  4,187.2 | 130.8 |  3.3% | interaction_muscl_renorm$interaction_muscl_renorm_mod_
# ||  10.8% |  2,412.6 | 148.4 |  6.3% | interaction_tvr_fluid$interaction_tvr_fluid_mod_
# ||   9.4% |  2,090.6 |  24.4 |  1.3% | interaction_gradker_fluid$interaction_gradker_fluid_mod_
# ||   4.9% |  1,081.6 |  61.4 |  5.9% | linearmuscl$muscl_linearreconstruction_mod_
# ||   3.9% |    863.2 |  26.8 |  3.3% | kernel_ts$kernel_mod_
# ||   1.4% |    315.1 |  37.9 | 11.7% | getneighborcells$octants_t_mod_
# ||   1.3% |    296.0 |  19.0 |  6.6% | getinteractionlist$interaction_lists_morton_mod_
# ||============================================================================
# |   4.2% |    936.2 |    -- |    -- | ETC
# ||----------------------------------------------------------------------------
# ||   1.2% |    262.4 |  28.6 | 10.7% | malloc_consolidate
# ||============================================================================
# |   3.8% |    837.8 |    -- |    -- | MPI
# ||----------------------------------------------------------------------------
# ||   2.0% |    448.4 | 432.6 | 53.6% | MPI_ALLREDUCE
# |=============================================================================
# 
# Table 2:  Profile by Group, Function, and Line

startline=`grep -n -m1 'Table 1:  Profile by Function' $in |cut -d: -f1`
endline=`grep -n -m1 'Table 2:  Profile by Group, Function, and Line' $in |cut -d: -f1`
if [ -z $endline ] ;then endline=`expr $startline + 50` ;fi
nlines=`expr $endline - $startline`
head -$endline $in |tail -$nlines |grep MPI_ |awk -FMPI_ '{print $2}'

grep -m1 
mpicallA=`grep -50 "$title" $in |grep -A2 "| MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
mpicallB=`grep -50 "$title" $in |grep -A3 "| MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
mpicallC=`grep -50 "$title" $in |grep -A4 "| MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`


#efface 
#efface 
#efface title='Table 1:  Profile by Function'
#efface #title='Table 1:  Profile by Function Group and Function'
#efface #tn=`grep -50 "$title" $in |grep \|Total |cut -d \| -f1 |tr -d " "`
#efface 
#efface craypatv=`grep 'CrayPat/X' $in |awk '{print $3}'`
#efface mppwidth=`grep 'Number of PEs ' $in |awk -F: '{print $2}'|tr -d " "`
#efface 
#efface userper=`   grep -50 "$title" $in |grep -m1 "| USER"            |cut -d \| -f2 |tr -d " "`
#efface mpicommper=`grep -50 "$title" $in |grep "| MPI$"            |cut -d \| -f2 |tr -d " "`
#efface mpiA=`      grep -50 "$title" $in |grep -A2 "| MPI$"|tail -1|cut -d \| -f3 |tr -d " "`
#efface mpiB=`      grep -50 "$title" $in |grep -A3 "| MPI$"|tail -1|cut -d \| -f3 |tr -d " "`
#efface mpiC=`      grep -50 "$title" $in |grep -A4 "| MPI$"|tail -1|cut -d \| -f3 |tr -d " "`
#efface #mpiD=`      grep -50 "$title" $in |grep -A5 "|MPI$"|tail -1|cut -d \| -f3 |tr -d " "`
#efface echo $in craypatv=$craypatv mppwidth=$mppwidth
#efface echo user%=$userper mpi%=$mpicommper mpiA=$mpiA mpiB=$mpiB mpiC=$mpiC $mppwidth
#efface #echo $in @$userper @ $mpicommper @$mpiA @$mpiB @$mpiC @$mpiD |tr -d " "|tr -d "%"
#efface mpicallA=`  grep -50 "$title" $in |grep -A2 "| MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
#efface mpicallB=`  grep -50 "$title" $in |grep -A3 "| MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
#efface mpicallC=`  grep -50 "$title" $in |grep -A4 "| MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
#efface #mpicallD=`  grep -50 "$title" $in |grep -A5 "|MPI$"|tail -1|cut -d \| -f7 |tr -d " "|cut -c5- |tr [a-z] [A-Z]`
#efface echo mpicallA=$mpicallA mpicallB=$mpicallB mpicallC=$mpicallC
#efface #echo $in @$userper @ $mpicommper @$mpicallA @$mpicallB @$mpicallC @$mpicallD |tr -d " "|tr -d "%"
#efface echo
#efface exit 0
#efface #speedup=`echo $t1 $tn |awk '{print $1/$2}'`
#efface #thspeedup=`echo $mppwidth $c1 |awk '{print $1/$2}'`
#efface #userper=`grep -50 "$title" $in |grep \|USER |cut -d \| -f2 |tr -d " "`
#efface #mpisyncper=`grep -50 "$title" $in |grep \|MPI_SYNC |cut -d \| -f2 |tr -d " "`
#efface #mpicommper=`grep -50 "$title" $in |grep "|MPI$" |cut -d \| -f2 |tr -d " "`
#efface #mpiper=`echo $mpisyncper $mpicommper |awk '{print $1+$2"%"}'`
#efface #etcper=`grep -50 "$title" $in |grep "|ETC$" |cut -d \| -f2 |tr -d " "`
#efface #echo $mppwidth @ $speedup @ $thspeedup @ $tn @ $userper @ $mpiper @ $mpicommper @ $mpisyncper @ $etcper @ $mppnppn @ $mppdepth @ $cn @ $cpersocket | tr -d " " | tr -d %
