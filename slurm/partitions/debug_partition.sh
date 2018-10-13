#!/bin/bash

# this is much simpler:
scontrol show job --oneliner |grep Partition=debug |awk '{print $1}' |cut -d= -f2 |awk '{print "scontrol show job",$0}' |sh
sinfo -p debug
sinfo -s -p debug

exit 0

