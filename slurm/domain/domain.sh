#!/bin/bash

n=$1
for i in `seq $n`;do for j in `seq $n`;do echo $i $j ;done;done |awk '$1*$2=='$n'{print $1,$2,$1*$2}' > $n
awk '$3='$n'{print $0,$1-$2}' $n | sort -nk4|more

