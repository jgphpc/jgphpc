#!/bin/bash

# Google sheet: OpenACC_Validation_Testsuite_SCS

in=$1
single_array_size=`grep ARRAY_SIZE= $in |cut -d= -f2`
copy_MBytes_sec=`grep ^Copy $in |awk '{print $2}'`
mul_MBytes_sec=`grep ^Mul $in |awk '{print $2}'`
add_MBytes_sec=`grep ^Add $in |awk '{print $2}'`
triad_MBytes_sec=`grep ^Triad $in |awk '{print $2}'`
dot_MBytes_sec=`grep ^Dot $in |awk '{print $2}'`

echo "$single_array_size,$copy_MBytes_sec,$mul_MBytes_sec,$add_MBytes_sec,$triad_MBytes_sec,$dot_MBytes_sec"
