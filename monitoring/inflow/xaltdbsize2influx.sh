#!/bin/bash

if [ -z $1 ] ; then
    indir=/apps/common/UES/sandbox/jgp/xalt/git/cscs/reports
    infile=o_size.log
    fullfile=$indir/$infile
else
    fullfile=$1
fi

# 2017-04-14T092331 = 0.05 0.05 5.03 491.88 388.06 466.23 988.52 0.05 158.77 797.38 1264.41 509.95 MB 5070.38
# 2017-04-14T100102 = 0.05 0.05 5.03 491.88 388.06 466.23 988.52 0.05 158.77 797.38 1264.41 509.95 MB 5070.38

if [ -f $fullfile ] ;then

while read line ;do

    # --- format from YYYY-MM-DDTHHMMSS to YYYY-MM-DDTHH:MM:SS
    # --- 2017-04-14T100102 ==> 2017-04-14T10:01:02
    datetime=`echo $line |awk '{print $1}'`
    YYYYMMDD=`echo $datetime |cut -dT -f1`
    HH=`echo $datetime |cut -dT -f2 |cut -c1-2`
    MM=`echo $datetime |cut -dT -f2 |cut -c3-4`
    SS=`echo $datetime |cut -dT -f2 |cut -c5-6`
    datetimeiso="${YYYYMMDD}T$HH:$MM:$SS"

    xalt_account=`echo $line |awk '{print $3}'` 
    xalt_env_name=`echo $line |awk '{print $4}'`
    xalt_function=`echo $line |awk '{print $5}'`
    xalt_link=`echo $line |awk '{print $6}'`
    xalt_object=`echo $line |awk '{print $7}'`
    xalt_run=`echo $line |awk '{print $8}'`
    xalt_total_env=`echo $line |awk '{print $9}'`
    xalt_user=`echo $line |awk '{print $10}'`
    join_link_function=`echo $line |awk '{print $11}'`
    join_link_object=`echo $line |awk '{print $12}'`
    join_run_env=`echo $line |awk '{print $13}'`
    join_run_object=`echo $line |awk '{print $14}'`
    xalt_total=`echo $line |awk '{print $16}'`

	# --- timestamp:
	# datetimeinflux=`date -d "$datetimeiso" +%s%N`
	datetimeinfluxsec=`date -d "$datetimeiso" +%s`

    # --- python:
    # mo use ~/easybuild/daint/haswell/modules/all
    # mll daint-gpu
    # mll influxdb/4.1.0-CrayGNU-2016.11-Python-2.7.12

cat << EOF > $fullfile.py
from inflow import Client                                 
client = Client('http://gorner02.cscs.ch:8086/influx_scs')
client.write('daint.scs.xaltdbsize', xalt_link=$xalt_link, timestamp=$datetimeinfluxsec)
client.write('daint.scs.xaltdbsize', xalt_object=$xalt_object, timestamp=$datetimeinfluxsec)
client.write('daint.scs.xaltdbsize', xalt_run=$xalt_run, timestamp=$datetimeinfluxsec)
client.write('daint.scs.xaltdbsize', xalt_total_env=$xalt_total_env, timestamp=$datetimeinfluxsec)
client.write('daint.scs.xaltdbsize', join_link_object=$join_link_object, timestamp=$datetimeinfluxsec)
client.write('daint.scs.xaltdbsize', join_run_env=$join_run_env, timestamp=$datetimeinfluxsec)
client.write('daint.scs.xaltdbsize', join_run_object=$join_run_object, timestamp=$datetimeinfluxsec)
client.write('daint.scs.xaltdbsize', xalt_total=$xalt_total, timestamp=$datetimeinfluxsec)
quit()
EOF

#     # from inflow import Client                                 
#     # client = Client('http://gorner02.cscs.ch:8086/influx_scs')
#         ## influx_scs.gorner = http://gorner02.cscs.ch:8086/influx_scs
#         ##             scsDB = http://tpc14.cscs.ch:8086/influxdb_scs
#     # grafana ==> http://gorner02.cscs.ch:8080/login
#     # 
#     #echo "client.write('daint.scs.xaltdbsize', xalt_account=$xalt_account, timestamp=$datetimeinfluxsec)"
#     #echo "client.write('daint.scs.xaltdbsize', xalt_env_name=$xalt_env_name, timestamp=$datetimeinfluxsec)"
#     #echo "client.write('daint.scs.xaltdbsize', xalt_function=$xalt_function, timestamp=$datetimeinfluxsec)"
#     echo "client.write('daint.scs.xaltdbsize', xalt_link=$xalt_link, timestamp=$datetimeinfluxsec)"
#     echo "client.write('daint.scs.xaltdbsize', xalt_object=$xalt_object, timestamp=$datetimeinfluxsec)"
#     echo "client.write('daint.scs.xaltdbsize', xalt_run=$xalt_run, timestamp=$datetimeinfluxsec)"
#     echo "client.write('daint.scs.xaltdbsize', xalt_total_env=$xalt_total_env, timestamp=$datetimeinfluxsec)"
#     #echo "client.write('daint.scs.xaltdbsize', xalt_user=$xalt_user, timestamp=$datetimeinfluxsec)"
#     #echo "client.write('daint.scs.xaltdbsize', join_link_function=$join_link_function, timestamp=$datetimeinfluxsec)"
#     echo "client.write('daint.scs.xaltdbsize', join_link_object=$join_link_object, timestamp=$datetimeinfluxsec)"
#     echo "client.write('daint.scs.xaltdbsize', join_run_env=$join_run_env, timestamp=$datetimeinfluxsec)"
#     echo "client.write('daint.scs.xaltdbsize', join_run_object=$join_run_object, timestamp=$datetimeinfluxsec)"
#     echo "client.write('daint.scs.xaltdbsize', xalt_total=$xalt_total, timestamp=$datetimeinfluxsec)"
	
done < $fullfile

else

    echo "$fullfile file not found"
    
fi

exit 0

#shell # --- bash:	
#shell 	# --- ProtocolLine:
#shell     echo "# $datetime "
#shell 	echo "INSERT osubw,sys=daint d2d=$d2d_maxsize $datetimeinflux"
#shell 	echo "INSERT osubw,sys=daint d2d32k=$d2d_32k $datetimeinflux"
#shell 	echo "INSERT osubw,sys=daint d2d8k=$d2d_8k $datetimeinflux"
#shell     # check with: SELECT * FROM "osubw"
#shell         # 2017-03-02T00:03:46 
#shell         # INSERT osubw,sys=daint d2d=8969.92 1488387826000000000
#shell         # INSERT osubw,sys=daint d2d32k=3339.63 1488387826000000000
#shell         # INSERT osubw,sys=daint d2d8k=2377.30 1488387826000000000
#shell         # > SELECT * FROM "osubw"
#shell 	  	# => name: osubw
#shell 	  	# => time                d2d     d2d32k  d2d8k   sys
#shell 	  	# => ----                ---     ------  -----   ---
#shell         # => 1488387826000000000 8969.92 3339.63 2377.3  daint
#shell         # => OK
#shell # -- influxdb+grafana:
#shell # 	for i in 2017* ;do ~/linux.git/hpc/gpu/g2g.sh $i ;done
#shell # use influxdb_daint_jg
#shell # 	INSERT osubw,sys=daint d2d=8694.24 1483203741000000000
#shell # 	INSERT osubw,sys=daint d2d=8925.43 1483290140000000000
#shell # 	INSERT osubw,sys=daint d2d=9029.11 1483376479000000000
#shell # 	INSERT osubw,sys=daint d2d=8991.65 1483376480000000000
#shell # 	INSERT osubw,sys=daint d2d=9029.93 1483462881000000000


# http://inflow.readthedocs.io/en/latest/querying.html#querying
# https://madra.cscs.ch/scs/PyRegression/issues/196
# http://tpc14.cscs.ch:81/dashboard/db/daint
# cd /apps/common/UES/sandbox/jgp/inflow.git/examples/

