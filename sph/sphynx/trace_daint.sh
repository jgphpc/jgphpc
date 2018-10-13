#!/bin/bash

export EXTRAE_HOME=$EBROOTEXTRAE
source $EXTRAE_HOME/etc/extrae.sh
export EXTRAE_CONFIG_FILE=$HOME/linux.git/sph/sphynx/extrae352_mpi+omp_sphynx.xml
# /apps/common/UES/sandbox/jgp/sphflow/sphynx.git/compile/extrae/extrae_sphynx.xml
export LD_PRELOAD=$EXTRAE_HOME/lib/libompitracef.so
# libmpitracef.so

## Run the desired program
$*
