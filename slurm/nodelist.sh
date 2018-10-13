#!/bin/bash
# sacct  -o NodeList%1000  -j 466131

# try https://github.com/hpc/gnawts/blob/master/bin/hostlist.py

in=$1
cat $in |sed -e "s-nid0\[--" -e "s-\]--" |tr "," "\n" > eff
while read line ; do
    start=`echo $line |cut -d- -f1`
      end=`echo $line |cut -d- -f2`
    if [ "$start" = "$end" ] ; then
        echo $start >> $in.eff
    else
        echo seq $start $end |sh >> $in.eff
    fi

done < eff

awk '{printf "%05d\n",$0}' $in.eff | sort > $in.all
rm -f eff $in.eff
