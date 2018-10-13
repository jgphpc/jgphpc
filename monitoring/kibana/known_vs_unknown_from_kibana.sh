#!/usr/bin/env bash

# Get list of slurm jobscript from kibana for a given jid and time window

# ./known_vs_unknown_from_kibana.sh 2018/04/01-00:00:00 2017/05/01-00:00:00 x x
## 04/2018:
##      2018/04/01-00:00:00 = 1522533600000 
##      2018/05/01-00:00:00 = 1525125600000
## 05/2018:
##      2018/05/01-00:00:00 = 1525125600000 
##      2018/05/10-00:00:00 = 1525903200000
##
# ./0.sh 2017/11/01-00:00:00 2017/12/01-00:00:00 pr29 4397855 
# awk '{print "./in_jid-out_srun.sh 2017/11/01-00:00:00 2017/12/01-00:00:00 pr29 ",$0}' $SCRATCH/kibana/avela/Nov.jids

# --- usage:
if [ $# -lt 3 ] ; then
   echo "USAGE : arg1=startdate arg2=enddate arg4=account arg3=jid"
   exit 0
fi
# exit 0

# --- parameters:
startdate=$1
enddate=$2
jid=$3
gid=$4
elastic_cscs='curl -s -XGET "http://sole01.cscs.ch:9200/slurm/_search?pretty"'
# sql='mysql -uuseradm -preadonly -h db.cscs.ch stat_csmon '

# --- functions:
# function date2epoch {
# {{{!
function date2epoch {
	# convert timestamp to epoch:
    # date2epoch 2017/11/01-00:00:00  # 1509490800 +000
    # date2epoch 2017/12/01-23:59:59  # 1512169199 +999
	timestamp=$1
	year=`echo $timestamp|awk '{print substr($0,1,4)}'`
	month=`echo $timestamp|awk '{print substr($0,6,2)}'`
	day=`echo $timestamp|awk '{print substr($0,9,2)}'`
	hour=`echo $timestamp|awk '{print substr($0,12,2)}'`
	min=`echo $timestamp|awk '{print substr($0,15,2)}'`
	sec=`echo $timestamp|awk '{print substr($0,18,2)}'`
	epoch=`echo $year $month $day $hour $min $sec |awk '{print mktime(sprintf("%d %d %d %d %d %d", $1,$2,$3,$4,$5,$6)) }'`
	#echo "$epoch @ $timestamp @"
	echo "$epoch"
}
  # !}}}

# function slurmscript_1jobid {
# {{{!
# --- find jobscript of 1jobid:
function slurmscript_1jobid {

# groupname=primarygid but account not always =groupname
# ==> search with account, NOT groupname 

t0=$1
t1=$2
jid=$3
#gid=$3
#jid=$4
#mkdir -p $SCRATCH/kibana/$gid

cat > eff.curl <<EOF

$elastic_cscs -d '{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query": "cluster:daint AND jobid:$jid",
            "analyze_wildcard": true
          }
        },
        {
          "range": {
            "@start": {
              "gte": $t0,
              "lte": $t1,
              "format": "epoch_millis"
            }
          }
        }
      ],
      "must_not": []
  }
},
    "size": 10
}
}'
EOF

#old $elastic_cscs -d '{
#old "query": {
#old   "bool": {
#old     "must": [
#old       {
#old         "query_string": {
#old           "query": "cluster:daint AND account:$gid AND jobid:$jid",
#old           "analyze_wildcard": true
#old         }
#old       },
#old       {
#old         "range": {
#old           "@start": {
#old             "gte": $t0,
#old             "lte": $t1,
#old             "format": "epoch_millis"
#old           }
#old         }
#old       }
#old     ],
#old     "must_not": []
#old   }
#old },
#old     "size": 10
#old }'
#old EOF

#jobidsfile=$SCRATCH/kibana/$gid/j$jid
jobidsfile=EFFACE/daint.$jid
#resfile=RES/daint.$jid
resfile=$jobidsfile 
. ./eff.curl > $jobidsfile

sacct -j $jid >> $resfile
echo >> $resfile
grep script $jobidsfile |sed -e "s-\\\n-\n-g" |sed -e "s-\\\t-\t-g" >> $resfile

grep -q script $jobidsfile
if [ $? -ne 0 ] ;then
    mv $resfile $resfile.bash
fi

echo "cat $jobidsfile*"
}
# !}}}

# --- convert dates into elasticsearch epoch_millis format:
t0=`date2epoch $startdate |awk '{print $0"000"}'`
t1=`date2epoch $enddate   |awk '{print $0"000"}'`
#echo $t0 $t1
#exit 0
#slurmscript_1jobid $t0 $t1 $gid $jid
slurmscript_1jobid $t0 $t1 $jid


exit 0

