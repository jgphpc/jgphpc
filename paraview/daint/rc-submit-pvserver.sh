#!/bin/bash

# tested Thu Jun 12 17:02:20 CEST 2014 for ParaView version 4.1


# usage
#echo "Usage : %1:Session name ($1)"
#echo "        %2:Job Wall Time ($2)"
#echo "        %3:server-num-nodes ($3)"
#echo "        %4:server-num-tasks-per-node ($4)"
#echo "        %5:server-binary ($5)"
#echo "        %6:server-port ($6)"
#echo "        %7:IP address forwarding the port ($7)"

# Create a temporary filename to write our launch script into
TEMP_FILE=`mktemp`
echo "Temporary FileName is :" $TEMP_FILE

nservers=$[$3 * $4]

# Create a job script
echo "#!/bin/bash"                                    >> $TEMP_FILE
echo "#SBATCH --job-name=$1"                          >> $TEMP_FILE
echo "#SBATCH --nodes=$3"                             >> $TEMP_FILE
echo "#SBATCH --ntasks-per-node=$4"                   >> $TEMP_FILE
echo "#SBATCH --ntasks=$nservers"                     >> $TEMP_FILE
echo "#SBATCH --time=$2"                              >> $TEMP_FILE
echo "#SBATCH --partition=viz"                              >> $TEMP_FILE
echo "#SBATCH --gres=gpu:1"                     >> $TEMP_FILE
echo "#SBATCH --constraint=startx"                              >> $TEMP_FILE
#echo "#SBATCH --reservation=maint"                              >> $TEMP_FILE
#echo "#SBATCH --output=/scratch/daint/jfavre/pvserver-OUT.log"   >> $TEMP_FILE
#echo "#SBATCH --error=/scratch/daint/jfavre/pvserver-ERR.log"    >> $TEMP_FILE
#echo "#SBATCH --exclude=nid00[436-443]"    >> $TEMP_FILE
#echo "#SBATCH --nodelist=nid0[0272-0279]"    >> $TEMP_FILE
#echo "#SBATCH --exclude=nid0[5248-5273,5275-5349,5351-5375]"    >> $TEMP_FILE

echo "export DISPLAY=:0"                         >> $TEMP_FILE
#echo "export PV_PLUGIN_DEBUG=1"                         >> $TEMP_FILE
echo "export LD_LIBRARY_PATH=/opt/cray/nvidia/default/lib64/:$LD_LIBRARY_PATH" >> $TEMP_FILE
echo ""                                               >> $TEMP_FILE

#echo "sleep 4" >> $TEMP_FILE
#echo "aprun -n $nservers -N $4 $5 -rc -ch=$7 -sp=$6" >> $TEMP_FILE
echo "aprun -n $nservers -N $4 $5 -rc -ch=$7 -sp=$6 --disable-xdisplay-test" >> $TEMP_FILE

# display the job submission for debug purposes
module swap PrgEnv-cray PrgEnv-gnu
module swap gcc/4.8.2 gcc/4.9.1
module load paraview
cat $TEMP_FILE

# submit the job

#/bin/rm /scratch/daint/jfavre/pvserver-???.log
/apps/daint/slurm/default/bin/sbatch $TEMP_FILE

# wipe the temp file
rm $TEMP_FILE
