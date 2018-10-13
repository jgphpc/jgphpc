#!/usr/bin/env python

# Data sources:
##             scsDB = http://tpc14.cscs.ch:8086/influxdb_scs
## influx_scs.gorner = http://gorner02.cscs.ch:8086/influx_scs

# http://inflow.readthedocs.io/en/latest/querying.html#querying
# https://madra.cscs.ch/scs/PyRegression/issues/196
# http://tpc14.cscs.ch:81/dashboard/db/daint
# cd /apps/common/UES/sandbox/jgp/inflow.git/examples/

# --- write to the DB on the server directly:
# ssh tpc14 ;influx -precision rfc3339 
# > use influxdb_scs
# > SHOW FIELD KEYS FROM "osubw"
# > SELECT * FROM "osubw"

# --- or send data to the DB from daint:
# ----------> ~/linux.git/hpc/gpu/g2g.sh

# module load daint-gpu
# module use /apps/daint/UES/jenkins/daint-gpu-jenkins-testPR/modules/all
# module load influxdb/4.0.0-CrayGNU-2016.11-Python-3.5.2

from inflow import Client
client = Client('http://tpc14.cscs.ch:8086/influxdb_scs')
# client = Client('http://gorner02.cscs.ch:8086/influx_scs')
# , precision='ms')
# client.write('temperature', value=21.3, timestamp=1476191999000)
# results = client.query('SELECT * FROM "temperature"')
# res = client.query('SELECT * FROM "osubw"')
res = client.query('SHOW FIELD KEYS FROM "osubw"')
print (res)
# client.query('SELECT * FROM "temperature"')
# client.query('SHOW FIELD KEYS from "temperature"')

# client.query('DROP SERIES FROM "temperature"')
# , epoch='s')

#cscs: datetimeinflux=`date -d "$datetime" +%s%N`
# date -d @1476191999000 --> Mon Aug 30 15:03:20 CEST 48748

