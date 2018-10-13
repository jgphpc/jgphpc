#!/bin/sh

# https://www.kernel.org/doc/Documentation/cpu-freq/boost.txt
# "1" = (boosting allowed)

cn=`uname -n`
boost=`cat /sys/devices/system/cpu/cpufreq/boost`
echo "$cn boost=$boost (1=on)"

