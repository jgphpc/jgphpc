#!/bin/bash

in=$1

# grep -q "Job credential expired" $in
# rc=$?
rc=1
if [ $rc -eq 0 ] ;then
    failed=1
    # echo yes
else
    # elapsed=`strings $in |tail -1 |awk '{print $7}'`
    elapsed=$in
    seconds=`echo $elapsed |awk -F: '{print $1*3600+$2*60+$3}'`
    echo "$seconds # $elapsed $in"
fi
# 02:45:20

