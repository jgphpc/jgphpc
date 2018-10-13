#!/bin/bash

# https://en.wikipedia.org/wiki/Coefficient_of_variation
## step1: this script
## step2: then jupyter script

in=$1
tmp1=`mktemp`
tmp2=`mktemp`
tmp3=`mktemp`
echo "tmp1=$tmp1 tmp2=$tmp2"
grep ' | thread' $in| tr -d \| > $tmp1

# --------------------------------------------------------------------------
# thread name:
threads=`awk '{print $2}' $tmp1`
i=0; for hhh in $threads ;do 
    i=`expr $i + 1`
    thread[$i]=$hhh
done

# --------------------------------------------------------------------------
# elapsed time:
times=`awk '{print $1}' $tmp1`
i=0; for ttt in $times ;do 
    i=`expr $i + 1`
    timings[$i]=$ttt
done

# --------------------------------------------------------------------------
# nid name:
nids=`grep ' | nid.' $in |tr -d \| |awk '{print $2}'`
i=0; for nid in $nids ;do 
    i=`expr $i + 1`
    nids[$i]="$nid"
done
# --------------------------------------------------------------------------
nprocesses=`wc -l $tmp1 |awk '{print $1}'`
nmpi=`grep ' | nid.' $in |wc -l`
nprocesses_per_node=`expr $nprocesses / $nmpi`
#echo nprocesses_per_node=$nprocesses_per_node
nnids=${#nids[@]}
nnidsm1=`expr $nnids - 1`
#i=0; for  in `seq $nnidsm1` ;do
#    echo "_ ${nids[$i]} _"
#done
# --------------------------------------------------------------------------
i=0; for nid in `seq $nnidsm1` ;do 
    i=`expr $i + 1`
    for jj in `seq $nprocesses_per_node` ;do
        echo ${nids[$i]}
    done
done > $tmp2
paste $tmp1 $tmp2 > $tmp3
# 192.293774  thread.21  nid.38
# 192.294707  thread.9  nid.37

# --------------------------------------------------------------------------
# print all:
echo '    timings_dict = {'
i=0; for i in `seq $nnidsm1` ;do
    echo "        '${nids[$i]}': {},"
done
echo '    }'

awk '{print "    timings_dict[xxx"$3"xxx].update({xxx"$2"xxx: "$1"})"}' $tmp3 |sed "s-xxx-'-g"
# https://stackoverflow.com/questions/1024847/add-new-keys-to-a-dictionary    
# my_dict['nid.3'].update({'thread.5':367.794018})
for i in `seq ${#computenode[@]}` ;do
    echo "    timings_dict['${computenode[$i]}'].update({'${thread[$i]}': ${timings[$i]}})"
done

# --------------------------------------------------------------------------
echo '===> jupyter/coefficient_of_variation.ipynb'
exit 0










