#!/bin/bash

srcf=$1
tmp1=/tmp/eff1.$$
tmp2=/tmp/eff2.$$

git log --pretty=oneline $srcf |head -n 10 |awk '{print $1}' > $tmp1
tail -n 9 $tmp1 > $tmp2
paste $tmp1 $tmp2 |awk -v q=$srcf '{print "git diff --no-ext-diff -w", substr($1,1,7), substr($2,1,7), q}' # > $tmp3

rm -f $tmp1 $tmp2
