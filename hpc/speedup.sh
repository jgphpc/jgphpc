#!/bin/bash

# {{{
# Strong scaling: solve problem more quickly than with a single proc.
#   Weak scaling: solve large problem in the same time as a single proc.
# Speedup(CN--->infinity) = 1 / (1-Parallelism)
# If Parallelism=90%  then Speedup <= 1/0.1 => "S <= 10x" !!!
# If Parallelism=100% then collective communication costs will increase with \#CN 
#         => app will not scale => overlap comp & comm.
# }}}
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

