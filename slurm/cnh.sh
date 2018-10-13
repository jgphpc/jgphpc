#!/bin/bash

# awk '{print "./cnh.sh ",$1,$2}' in |sh |awk '{print "cnh="$0}'

cn=$1
dureeh=$2
dureesec=`echo "$dureeh" |tr : " " |awk '{print $1*3600+$2*60+$3}'`

# function awkhms(s) { h=int($0/3600); s=s-(h*3600); m=int(s/60); s=s-(m*60); printf("%d:%02d:%02d\n", h, m, s); }
function hms {
    seconds=$1
    hours=$((seconds / 3600))
    seconds=$((seconds % 3600))
    minutes=$((seconds / 60))
    seconds=$((seconds % 60))
    echo $hours $minutes $seconds |awk '{printf "%d:%02d:%02d\n",$1,$2,$3}'
    #echo "$hours:$minutes:$seconds" 
    #echo "$hours hour(s) $minutes minute(s) $seconds second(s)"
}

cnh=`echo $cn $dureesec |awk '{print $1*$2}' `
hms $cnh

# |awk '{print "date -d@"$0" -u +%H:%M:%S"}' |sh`
# echo $cnh
