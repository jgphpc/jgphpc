#!/bin/bash

# awk -Fvalue: '{print $2}' cp2k_cpu_check.log |cut -d, -f1 > /tmp/eff
in=$1

min=`sort -nk 1 $in |head -1 |awk '{printf "%.2f",$0}'`
max=`sort -nk 1 $in |tail -1 |awk '{printf "%.2f",$0}'`
avg=`sort -nk 1 $in |awk '{s=s+$0}END{printf "%.2f",s/NR}'`

echo "$min $avg $max # $in"
