#!/bin/bash

# Data sources:
##             scsDB = http://tpc14.cscs.ch:8086/influxdb_scs
## influx_scs.gorner = http://gorner02.cscs.ch:8086/influx_scs

# http://inflow.readthedocs.io/en/latest/querying.html#querying
# https://madra.cscs.ch/scs/PyRegression/issues/196
# http://tpc14.cscs.ch:81/dashboard/db/daint
# cd /apps/common/UES/sandbox/jgp/inflow.git/examples/

# -- influxdb+grafana:
# 	for i in 2017* ;do ~/linux.git/hpc/gpu/g2g.sh $i ;done
# use influxdb_daint_jg
# 	INSERT osubw,sys=daint d2d=8694.24 1483203741000000000
# 	INSERT osubw,sys=daint d2d=8925.43 1483290140000000000
# 	INSERT osubw,sys=daint d2d=9029.11 1483376479000000000
# 	INSERT osubw,sys=daint d2d=8991.65 1483376480000000000
# 	INSERT osubw,sys=daint d2d=9029.93 1483462881000000000
jenkinsdir=/apps/daint/UES/jenkins/nightly-dev
logfile=gpu/g2g_osu_microbenchmark_p2p_gpu/PrgEnv-cray/g2g_osu_microbenchmark_p2p_gpu.out
datetime=$1     # new=2017-03-13_00-01-40 (old was 2017-01-24T15:13:37)
fullfile=$jenkinsdir/$datetime/$logfile
if [ -f $fullfile ] ;then

    # --- old date format:
    datetimeiso=$datetime

    # --- new date format:
#     # format $datetime from YYYY-MM-DD_HH-MM-SS to YYYY-MM-DDTHH:MM:SS
#     YYYY=`echo $datetime |cut -d- -f1`
#     MM=`echo $datetime |cut -d- -f2`
#     DD=`echo $datetime |cut -d- -f3 |cut -d_ -f1`
#     HHMMSS=`echo $datetime |cut -d_ -f2 |tr "-" :`
#     datetimeiso=$YYYY-$MM-$DD'T'$HHMMSS

	# --- timestamp:
	datetimeinflux=`date -d "$datetimeiso" +%s%N`
	datetimeinfluxsec=`date -d "$datetimeiso" +%s`
	
	# --- OSU MPI-CUDA Bandwidth Test:
	# Send Buffer on DEVICE (D) and Receive Buffer on DEVICE (D)
	# Size        Bandwidth (MB/s)
	d2d_maxsize=`grep ^4194304 $fullfile |awk '{print $2}'`
	d2d_32k=`grep ^32768   $fullfile |awk '{print $2}'`
	d2d_8k=`grep ^8192  $fullfile |awk '{print $2}'`

#    #    #  ######  #       #    #  #    #  #####   #####
#    ##   #  #       #       #    #   #  #   #    #  #    #
#    # #  #  #####   #       #    #    ##    #    #  #####
#    #  # #  #       #       #    #    ##    #    #  #    #
#    #   ##  #       #       #    #   #  #   #    #  #    #
#    #    #  #       ######   ####   #    #  #####   #####
# --- python:
    # from inflow import Client                                 
    # client = Client('http://gorner02.cscs.ch:8086/influx_scs')
    # echo "client.write('daint.scs.osubw', d2d=$d2d_maxsize, timestamp=$datetimeinfluxsec)"

# --- bash:	
	# --- ProtocolLine:
    echo "# $datetime "
	echo "INSERT osubw,sys=daint d2d=$d2d_maxsize $datetimeinflux"
	echo "INSERT osubw,sys=daint d2d32k=$d2d_32k $datetimeinflux"
	echo "INSERT osubw,sys=daint d2d8k=$d2d_8k $datetimeinflux"
    # check with: SELECT * FROM "osubw"
        # 2017-03-02T00:03:46 
        # INSERT osubw,sys=daint d2d=8969.92 1488387826000000000
        # INSERT osubw,sys=daint d2d32k=3339.63 1488387826000000000
        # INSERT osubw,sys=daint d2d8k=2377.30 1488387826000000000
        # > SELECT * FROM "osubw"
	  	# => name: osubw
	  	# => time                d2d     d2d32k  d2d8k   sys
	  	# => ----                ---     ------  -----   ---
        # => 1488387826000000000 8969.92 3339.63 2377.3  daint
        # => OK

	 
fi

# SELECT "d2d8k" FROM "osubw" WHERE time > 1483225200000ms and time < 1514761199999ms  limit 2

#  date -d 2017-01-24T15:13:37 +%s%N   # => 1485245617000000000
#  > INSERT osubw,sys=daint d2d=34.2 1485245617000000000
#  > SELECT * FROM osubw               # => 2017-01-24T08:13:37Z
# 2016-12-07T00:01:19/g2g_osu_microbenchmark_p2p_gpu/PrgEnv-cray/g2g_osu_microbenchmark_p2p_gpu.out


exit 0








# -- gnuplot:
# /apps/daint/UES/jenkins/nightly-dev/2017-02-08T00:02:14/g2g_osu_microbenchmark_p2p_gpu
# /apps/common/UES/sandbox/jgp/mvapich2.trunk/osu_benchmarks/532JG/GNUPLOT
in=eff.4194304

minbw=`awk '{print $3}' $in |sort -nk 1 |head -1`
maxbw=`awk '{print $3}' $in |sort -nk 1 |tail -1`
meanbw=`awk '{s=s+$3}END{print s/NR}' $in`

# in=$1
set xdata time
set timefmt "_%Y-%m-%dT%H-%M-%S"
show timefmt
set format x "%Y-%m-%d"
set grid
set ylabel "D2D Bandwidth for size=4194304 (MB/s)"
set xlabel "PizDaint"
set xtics rotate by -45
set logscale y
# set grid mytics 
# set yrange [5000:10000]
plot "eff.4194304" u 1:3 w lp t "osu_bw_mpicuda_D2D", 8810.18 t "avg bw"


# Size        Bandwidth (MB/s)
# Format       Explanation
# %d           day of the month, 1--31
# %m           month of the year, 1--12
# %y           year, 0--99
# %Y           year, 4-digit
# %j           day of the year, 1--365
# %H           hour, 0--24
# %M           minute, 0--60
# %s           seconds since the Unix epoch (1970-01-01, 00:00 UTC)
# %S           second, 0--60
# %b           three-character abbreviation of the name of the month
# %B           name of the month




