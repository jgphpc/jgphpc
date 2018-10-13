#!/bin/sh

for i in `seq 0 19` ;do
    cn=`uname -n`
    gov=`cat /sys/devices/system/cpu/cpu$i/cpufreq/scaling_governor`
    echo "$cn c$i $gov"
done
