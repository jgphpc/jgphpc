#!/bin/bash

in=$1   # col1=cn / col2=timing

czero=`head -1 $in |awk '{printf "%05d", $1}'`
tzero=`head -1 $in |awk '{printf "%.4f", $2}'`
while read cn tn ;do
    ispeedup=`echo $cn $czero |awk '{printf "%.0f", $1/$2}'`
     speedup=`echo $tzero $tn |awk '{printf "%.2f", $1/$2}'`
     efficiency=`echo  $speedup $cn $czero |awk '{printf "%5.1f%", $1/$2*$3*100}'`
    t=`echo $tn |awk '{printf "%8.4f", $1}'`
    # echo "$cn $t $speedup/$ispeedup $efficiency"
    #markdown: 
    echo "| $cn | $speedup/$ispeedup | $efficiency | $t |" 
    #googledoc: echo "  $cn $speedup $ispeedup $efficiency $t "
done < $in

