#!/bin/bash

# awk '{print "./sphflow_run.sh "$1,$2,$3}' in/dx.weak
# awk '{print "./sphflow_run.sh "$1,$2,$3}' in/dx.strong

# PW=/apps/common/UES/sandbox/jgp/sphflow/dom@CRAY-8.6.1@prgenv-6.0.UP04@mpi-7.6.3@libsci-17.11.1@hdf5p-1.8.16@cpu-haswell@hsn-aries/CMAKE/bin
PW=/apps/common/UES/sandbox/jgp/sphflow/dom@PGI-@prgenv-6.0.UP04@mpi-7.6.3@libsci-@hdf5p-1.8.16@cpu-haswell@hsn-aries/CMAKE/bin

nppc=$1
dx=$2
c=$3
DD=$nppc'_'$dx'_'$c
where=1

# --- sphflow:
if [ $where=1 ] ;then

## dom-gpu max = 16cn = 192c
cat > .eff << EOF
cd $DD
~/sbatch.sh dom 30 $PW/$EXE.x $c 12 1 1 1 "-Cgpu -d singleton" "*.nml dambreak0.h5" "/usr/bin/time -p"
cd -
EOF

echo "#debug mode:"
#cat .eff
. .eff

exit 0
fi

# --- presph:
if [ $where=0 ] ;then

cat > .eff << EOF
mkdir -p $DD
cd $DD
cp ../in/*dat . 
sed "s-XXXX-$dx-" ../in/dambreak.nml > dambreak.nml
~/sbatch.sh dom 30 ~/bin/presph 48 12 1 1 1 -Cgpu *.nml
cd -
EOF

echo "#debug mode:"
cat .eff
#. .eff

fi
