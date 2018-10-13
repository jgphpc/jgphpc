#!/bin/bash

# export EXTRAE_HOME=$EBROOTEXTRAE
source $EXTRAE_HOME/etc/extrae.sh

export EXTRAE_CONFIG_FILE=$HOME/linux.git/sph/sphflow/extrae352_sphflow_mn4.xml

export LD_PRELOAD=$EXTRAE_HOME/lib/libompitracef.so
# libmpitracef.so

## Run the desired program
$* ./square.nml ./square0.h5 
# $*

