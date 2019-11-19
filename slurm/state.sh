#!/bin/bash

in=$1   # dca.res.all
awk '{print "scontrol show nodes nid"$0}' $in |sh |egrep "State=|NodeName=" |awk '{print $1}' > $in.state
grep ^State= $in.state |sort -u
