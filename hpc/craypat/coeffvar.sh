#!/bin/bash

# https://en.wikipedia.org/wiki/Coefficient_of_variation
## step1: this script
## step2: then jupyter script

##  CV = c/u   where c is the standard deviation and u the mean.
##  We have 4 MPI ranks (N=4). 
##  Each rank will use 12 OpenMP threads. 
##  We take for each MPI rank the time of the worst OpenMP thread as Trank. 
##  We calculate the mean of the worst times:
##      u = (Tr0 +... + TrN)/N
##  and then the standard deviation as 
##      c = sqrt[(Tri - u)/N]
##      c = sqrt[sum{(Tri - u)^2}/(N)] ? N-1 ?

in=$1
tmp1=`mktemp`
tmp2=`mktemp`
echo "tmp1=$tmp1 tmp2=$tmp2"
grep ' | thread' $in| tr -d \| > $tmp1

# --------------------------------------------------------------------------
times=`awk '{print $1}' $tmp1`
i=0; for ttt in $times ;do 
    i=`expr $i + 1`
    timings[$i]=$ttt
done

# --------------------------------------------------------------------------
threads=`awk '{print $2}' $tmp1`
i=0; for hhh in $threads ;do 
    i=`expr $i + 1`
    thread[$i]=$hhh
done

# --------------------------------------------------------------------------
# list of nids = mpi tasks:
nmpi=`grep ' | nid.' $in |wc -l`
nids=`grep ' | nid.' $in |tr -d \| |awk '{print $2}'`
#echo "nids=$nids"
i=0; for cn in $nids ;do 
    i=`expr $i + 1`
    nids[$i]="$cn"
done

nnids=${#nids[@]}
nnidsm1=`expr $nnids - 1`
i=0; for i in `seq $nnidsm1` ;do
    echo "_ ${nids[$i]} _"
done
#echo "#nids=${#nids[@]} / ${nids[1]} / ${nids[2]}"

# --------------------------------------------------------------------------
# list of openmp threads:
nopenmp=`grep 'Numbers of Threads per PE:' $in |awk '{print $6}'`

echo > $tmp2
for mpi in `seq $nnidsm1` ;do
    for omp in `seq $nopenmp` ;do
        echo ${nids[$mpi]} >> $tmp2
    done
    #echo
done


# --------------------------------------------------------------------------
# validation of mpi tasks and openmp threads:
nmpiomp1=`echo $nmpi $nopenmp |awk '{print $1*$2}'`
nmpiomp2=`wc -l $tmp1 |awk '{print $1}'`

if [ $nmpiomp1 -ne $nmpiomp2 ] ;then
    echo "nmpiomp1=$nmpiomp1 != nmpiomp2=$nmpiomp2 (ko)"
    nmpiomp1=12
    exit 0
else
    echo "nmpiomp1=$nmpiomp1 == nmpiomp2=$nmpiomp2 (ok)"
fi

# --------------------------------------------------------------------------
computenids=`awk '{print $1}' $tmp2`
i=0; for ccc in $computenids ;do 
    i=`expr $i + 1`
    computenode[$i]=$ccc
done
# echo ${computenode[@]}

# --------------------------------------------------------------------------
# print all:
echo '    timings_dict = {'
i=0; for i in `seq $nnidsm1` ;do
    echo "        '${nids[$i]}': {},"
done
echo '    }'
   
# https://stackoverflow.com/questions/1024847/add-new-keys-to-a-dictionary    
# my_dict['nid.3'].update({'thread.5':367.794018})
for i in `seq ${#computenode[@]}` ;do
    echo "    timings_dict['${computenode[$i]}'].update({'${thread[$i]}': ${timings[$i]}})"
done
#for i in `seq ${#computenode[@]}` ;do
#    echo "| ${computenode[$i]} | ${thread[$i]} | ${timings[$i]} |"
#done > $tmp1
#echo "nids=${nids[@]} #=${#nids[@]}"
#echo "computenids=$computenids"
#echo "computenode=${computenode[@]}"
#exit 0




echo '===> jupyter/coefficient_of_variation.ipynb'
exit 0

# --------------------------------------------------------------------------
# slowest openmp thread for each mpi rank:
cnodes=`awk -F \| '{print $2}' $tmp1 |sort |uniq`
ncnodes=`awk -F \| '{print $2}' $tmp1 |sort |uniq |wc -l |awk '{print $1}'`
#echo "cn=$cnodes #=$ncnodes"

slowesttsum=0
for cnid in $cnodes ;do
    slowestt=`grep "| $cnid |" $tmp1 |awk -F\| '{print $4}' |tr -d " "|sort -nk1 |head -1`
    #fastestt=`grep "| $cnid |" $tmp1 |awk -F\| '{print $4}' |tr -d " "|sort -nk1 |tail -1`
    #echo $cnid / $slowestt / $fastestt 
    slowesttsum=`echo $slowesttsum $slowestt |awk '{print $1+$2}'`
done

# --------------------------------------------------------------------------
# uuu=mean
uuu=`echo $slowesttsum $ncnodes|awk '{print $1/$2}'`
echo uuu=$uuu

# --------------------------------------------------------------------------
# ccc=standard deviation
slowestt=0
slowestt_uuu=0
slowestt_uuu_sum=0
for cnid in $cnodes ;do
    slowestt=`grep "| $cnid |" $tmp1 |awk -F\| '{print $4}' |tr -d " "|sort -nk1 |head -1`
    slowestt_uuu=`echo $slowestt $uuu |awk '{print ($1-$2)^2}'`
    slowestt_uuu_sum=`echo $slowestt_uuu_sum $slowestt_uuu |awk '{print $1+$2}'`
done
ccc=`echo $slowestt_uuu_sum $ncnodes|awk '{print sqrt($1/$2)}'`
echo ccc=$ccc

cv=`echo $ccc $uuu |awk '{print $1/$2}'`
echo cv=$cv
exit 0
#for i in `seq ${#computenode[@]}` ;do
#    echo ${timings[$i]}
#done

# /project/c16/sphynx/coefficient_of_variation/rotating_square_patch_3D/daint

# --------------------------------------------------------------------------
craypatv=`grep 'CrayPat/X' $in |awk '{print $3}'`
#mppwidth=`grep 'Number of PEs ' $in |awk -F: '{print $2}'|tr -d " "`
cn=`grep 'Numbers of PEs per Node:' $in |awk '{print $11}'`

# --------------------------------------------------------------------------
echo "in=$in"
echo "craypatv=$craypatv"
echo "cn=$cn"
