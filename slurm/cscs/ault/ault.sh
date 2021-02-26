#!/bin/bash

in=00
# in=11
while read line ;do
    pp=`echo "$line" |awk '{print $1}' |cut -d= -f2`
    nn=`echo "$line" |awk '{print $2}' |cut -d= -f2 |xargs hostlist -e |sed "s-ault--g"`
    ss=`seq -w 40`
    res=`seq -w 40 |awk '{printf "0"}'`
    xx=$res
    for yes in $nn ;do
        echo -n $pp:
        # unset xx
        index=0
        for cn in $ss ;do
            index=`expr $index + 1` 
            if [ "$yes" = "$cn" ] ; then
                xx=`echo $xx |sed s/./1/$index`
                # xx="$xx"1
            # else
            #     xx="$xx"0
            fi
        done
        # res=`expr $xx + $res`
        # echo $res
        echo $xx
    # echo
    done
done < $in
