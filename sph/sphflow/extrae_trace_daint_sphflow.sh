#!/bin/bash

export EXTRAE_HOME=$EBROOTEXTRAE
source $EXTRAE_HOME/etc/extrae.sh
# export EXTRAE_CONFIG_FILE=./extrae.xml
export EXTRAE_CONFIG_FILE=~/linux.git/sph/sphflow/extrae352_sphflow_daint.xml
export LD_PRELOAD=$EXTRAE_HOME/lib/libmpitracef.so
#export LD_PRELOAD=$EXTRAE_HOME/lib/libompitracef.so
#omp: export LD_PRELOAD=$EXTRAE_HOME/lib/libompitracef.so

## Run the desired program
$* ./square.nml ./square0.h5 
# ./sphflow AEEP_Test_clr11-12v.nml AEEP_Test_clr11-12v3.h5
# $* "$@"
