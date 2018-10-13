#!/bin/bash

dirs=(gpu mc)
for dir in ${dirs[@]}; do

    files=(`ls $APPS/UES/jenscscs/regression/production/logs/$dir/*.log`)
    mkdir -p $dir

for file in ${files[@]}; do

    checkname=`basename $file`
    checkname=$dir/$checkname
    rm -rf $checkname

    ids=(`grep -ir id $file | awk '{print $3,$5,$7}' | grep -v INFO | awk -F'=' '{print $2}' | awk -F')' '{print $1, $2, $3}' | awk -F':' '{print $1, $2}' | awk -F'(' '{print $1,$2}' | awk -F',' '{print $1, $2, $3}' | awk '{print $1}'`)

    values=(`grep -ir id $file | awk '{print $3,$5,$7}' | grep -v INFO | awk -F'=' '{print $2}' | awk -F')' '{print $1, $2, $3}' | awk -F':' '{print $1, $2}' | awk -F'(' '{print $1,$2}' | awk -F',' '{print $1, $2, $3}' | awk '{print $2}'`)

    refs=(`grep -ir id $file | awk '{print $3,$5,$7}' | grep -v INFO | awk -F'=' '{print $2}' | awk -F')' '{print $1, $2, $3}' | awk -F':' '{print $1, $2}' | awk -F'(' '{print $1,$2}' | awk -F',' '{print $1, $2, $3}' | awk '{print $3}'`)

    percentage=(`grep -ir id $file | awk '{print $3,$5,$7}' | grep -v INFO | awk -F'=' '{print $2}' | awk -F')' '{print $1, $2, $3}' | awk -F':' '{print $1, $2}' | awk -F'(' '{print $1,$2}' | awk -F',' '{print $1, $2, $3}' | awk '{print ($2-$3)*100.0/$3}'`)

    for ((i=0; i < ${#ids[@]}; i++)); do

        #echo -e $i    ${ids[$i]}    ${values[$i]}    ${refs[$i]}    ${percentage[$i]}
        jobid=${ids[$i]}
        nodelist=`sacct -j ${jobid} -o nodelist%500 | tr -d ' ' | tail -1`
        number_of_groups=`scontrol show nodes $nodelist | grep -i activefeatures | sort -u | awk -F ',' '{print $4}' | wc -l`

        #echo ${number_of_groups}"   "${percentage[$i]}"   "${values[$i]} >> $checkname
        echo ${number_of_groups}"   "${values[$i]} >> $checkname
    done
    #echo

done

done
