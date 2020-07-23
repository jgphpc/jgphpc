#!/bin/bash

in1=$1

# sqpatch_xsmall_mpi+omp_001mpi_001omp_30n_10steps
# - daint:gpu
#    - PrgEnv-cray
#       * num_tasks: 1
#       * Elapsed: 8.6628 s
#       * Final step: 10
#       * Total Neighbors: 6707644
#       * Avg neighbor count per particle: 248
#       * Total energy: 20814700000.0 erg
#       * Internal energy: -254600.0 erg

echo "mydata = {}"
while read l ;do
    echo "$l" |grep -q sqpatch ;rc1=$?
    if [ $rc1 -eq 0 ] ;then 
        exe=`echo "$l" |cut -d_ -f3`
        echo "mydata['$exe'] = {}"

        dim=`echo "$l" |cut -d_ -f2`
        echo "mydata['$exe']['$dim'] = {}"
    fi
done < $in1 |sort -u

while read l ;do
    echo "$l" |grep -q sqpatch ;rc1=$?
    echo "$l" |grep -q PrgEnv- ;rc2=$?
    echo "$l" |grep -q num_tasks ;rc3=$?
    echo "$l" |grep -q Elapsed: ;rc4=$?
    echo "$l" |grep -q "Total Neighbors:" ;rc5=$?
    echo "$l" |grep -q "Avg neighbor count" ;rc6=$?
    echo "$l" |grep -q "Total energy:" ;rc7=$?
    echo "$l" |grep -q "Internal energy:" ;rc8=$?
    if [ $rc1 -eq 0 ] ;then 
        exe=`echo "$l" |cut -d_ -f3`
        dim=`echo "$l" |cut -d_ -f2`
        # echo "'ntasks': $res,"
    fi
    if [ $rc2 -eq 0 ] ;then 
        # echo "mydata['$exe']['$dim'] = {"
        pe=`echo "$l" |awk '{print $2}'`
        # echo "mydata['$exe']['$dim']['$pe'] = []"
    fi

    if [ $rc3 -eq 0 ] ;then res3=`echo "$l" |awk '{print $3}'`; fi #echo "'ntasks': $res,";fi
    if [ $rc4 -eq 0 ] ;then res4=`echo "$l" |awk '{print $3}'`; fi #echo "'elapsed': $res,";fi
    if [ $rc5 -eq 0 ] ;then res5=`echo "$l" |awk '{print $4}'`; fi #echo "'tot_neighb': $res," ;fi
    if [ $rc6 -eq 0 ] ;then res6=`echo "$l" |awk '{print $7}'`; fi #echo "'avg_neighb': $res," ;fi
    if [ $rc7 -eq 0 ] ;then res7=`echo "$l" |awk '{print $4}'`; fi #echo "'tot_nrg': $res," ;fi
    if [ $rc8 -eq 0 ] ;then 
        res8=`echo "$l" |awk '{print $4}'`
        echo "mydata['$exe']['$dim']['$pe'] = [$res5, $res6, $res7, $res8]"
        #ko echo "mydata['$exe']['$dim']['$pe'].append([$res5, $res6, $res7, $res8])"
    fi #echo "'int_nrg': $res,}" ;fi

    # if [ -z "$res" ] ;then res=-1 ;fi ;echo "'tot_neighb': $res," ;fi
    # if [ -z "$res" ] ;then res=-1 ;fi ;echo "'avg_neighb': $res," ;fi
    # if [ -z "$res" ] ;then res=-1 ;fi ;echo "'tot_nrg': $res," ;fi
    # if [ -z "$res" ] ;then res=-1 ;fi ;echo "'int_nrg': $res,}" ;fi
done < $in1 # | sort -u
