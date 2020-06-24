#!/bin/bash

# TODO: get list of github.com/PR

srcf=$1
tmp1=/tmp/eff1.$$
tmp2=/tmp/eff2.$$

myos=`uname -s`
if [ "$myos" = Darwin ] ;then
    myrev='tail -r'
else
    myrev='tac'
fi

log_size=`git log --pretty=oneline $srcf |wc -l`
if [ $log_size -lt 5 ] ;then
    back_to=$log_size
else
    back_to=10
fi
back_to_m1=`expr $back_to - 1`
git log --pretty=oneline $srcf |head -n $back_to |$myrev |awk '{print $1}' > $tmp1
tail -n $back_to_m1 $tmp1 > $tmp2
paste $tmp1 $tmp2 \
|awk -v q=$srcf '{ss="git diff --no-ext-diff -w "substr($1,1,7)" "substr($2,1,7)" "q ;print ss}' \
|head -$back_to_m1 # > $tmp3

rm -f $tmp1 $tmp2
