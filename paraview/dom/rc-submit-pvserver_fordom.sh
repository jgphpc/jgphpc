#!/bin/bash -l

# tested Mon Mar 27 09:08:05 CEST 2017 for ParaView 5.3


# usage
echo "\$1 = $1 = session_job_name"
echo "\$2 = $2 = maxtime"
echo "\$3 = $3 = nodes"
echo "\$4 = $4 = tasks per node"
echo "\$5 = $5 = port"
echo "\$6 = $6 = host "
echo "\$7 = $7 = version (unused)"

jobname=$1
maxtime=$2
maxnodes=$3
taskspernode=$4
nservers=$[$3 * $4]
myport=$5
myhost=$6
myversion=$7

# Create a temporary filename to write our launch script into
TEMP_FILE=`mktemp`
echo "Temporary FileName is :" $TEMP_FILE
echo "PWD=$PWD"


# Create a job script
echo "#!/bin/bash"                                     > $TEMP_FILE
echo "#SBATCH --job-name=$jobname"                    >> $TEMP_FILE
echo "#SBATCH --nodes=$maxnodes"                      >> $TEMP_FILE
echo "#SBATCH --ntasks-per-node=$taskspernode"        >> $TEMP_FILE
echo "#SBATCH --ntasks=$nservers"                     >> $TEMP_FILE
echo "#SBATCH --time=$maxtime"                        >> $TEMP_FILE
echo "#SBATCH --constraint=gpu"                       >> $TEMP_FILE
echo "#SBATCH --exclusive"                            >> $TEMP_FILE
echo "#SBATCH --output=$SCRATCH/o"                    >> $TEMP_FILE
echo "#SBATCH --error=$SCRATCH/o"                     >> $TEMP_FILE
echo "#export PV_PLUGIN_DEBUG=1"                      >> $TEMP_FILE
#
echo "module load daint-gpu"                          >> $TEMP_FILE

echo "module unload ddt xalt"                         >> $TEMP_FILE
#echo "export HDF5_DISABLE_VERSION_CHECK=2"            >> $TEMP_FILE
#if [ "$7" = "GNU-5.4" ]; then
#    echo "module load ParaView/5.4.1-CrayGNU-17.08-EGL"  >> $TEMP_FILE
#elif [ "$7" = "GNU-5.5" ]; then
#    echo "module load ParaView/5.5.0-CrayGNU-17.08-EGL"  >> $TEMP_FILE
#fi
#

echo "module use /scratch/snx3000tds/jfavre/daint/modules/all" >> $TEMP_FILE
echo "module load ParaView/5.5.1-CrayGNU-17.08-EGL"         >> $TEMP_FILE

#echo "module use /apps/dom/UES/jenkins/6.0.UP04/gpu/easybuild-1/modules/all" >> $TEMP_FILE
#echo "module load ParaView/5.5.1-CrayGNU-17.08-EGL"   >> $TEMP_FILE
#echo "module rm Boost/1.65.0-CrayGNU-17.08-python3; module load /apps/dom/UES/jenkins/6.0.UP04/gpu/easybuild-1/modules/all/Boost/1.65.0-CrayGNU-17.08-python3"                                      >> $TEMP_FILE
#echo "export LD_LIBRARY_PATH=/opt/python/3.6.1.1/lib:\$LD_LIBRARY_PATH" >> $TEMP_FILE
#echo "module rm cray-python/17.06.1"                  >> $TEMP_FILE
#echo "module rm cray-python/3.6.1.1"                  >> $TEMP_FILE

echo "module list -t"                                 >> $TEMP_FILE
echo 'echo pvserver=`which pvserver`'                 >> $TEMP_FILE
echo ""                                               >> $TEMP_FILE
echo "set -x ;pwd"                                    >> $TEMP_FILE
echo "srun --cpu_bind=sockets \`which pvserver\` -rc -sp=$myport -ch=$myhost" >> $TEMP_FILE
echo "set +x ;pwd"                                    >> $TEMP_FILE

# --server-port=opt -sp=opt  What port should the combined server use to connect to the client. (default 11111).
# --client-host=opt -ch=opt  Tell the data|render server the host name of the client, use with -rc.

cat $TEMP_FILE

# submit the job
sbatch $TEMP_FILE

# wipe the temp file
rm $TEMP_FILE
