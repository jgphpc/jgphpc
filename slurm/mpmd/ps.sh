#!/bin/bash

out=o_ps
echo tt: `date +%Y/%m/%d-%H:%M:%S-%s.%N` > $out

for i in `seq 5` ;do
    echo T: `date +%Y/%m/%d-%H:%M:%S-%s.%N`
    ps -u piccinal -ww -o pid,ppid,etime,stat,command
    sleep 1
done >> $out

echo tt: `date +%Y/%m/%d-%H:%M:%S-%s.%N` >> $out
# top -u piccinal -b -d1 -n8 &> o_2 &
