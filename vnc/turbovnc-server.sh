#!/bin/bash
#SBATCH --job-name="T-VNCs"
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=6g
#SBATCH --time=1:00:00
##SBATCH --gres=gpu:1
#SBATCH --partition=h-interactive
##SBATCH --nodelist=leone30
#SBATCH --output=eff_ovnc
#SBATCH  --error=eff_ovnc

#======START=============================================

# WARNING: This script helps starting a TurboVNC session. However 
#          this script does not handle correctly multiple Turbo-VNC session of the SAME USER.

. /etc/profile.d/modules.bash
module load libjpegturbo/1.4.2
module load virtualgl/2.4.1
module load cuda/7.5.18
module load turbovnc/2.0.1

VNC_GEOM=1920x1080
VNC_NAME=$USER@$SLURM_JOB_NODELIST
VNC_SCRIPT="leone_TurboVNCs.sh"
VNC_SCRIPT_VERSION="$VNC_SCRIPT version 1.3 (Wed Jan 20 10:02:00 CET 2016)"

OPTIND=1
while getopts  "g:d:n:hv" flag
do
#  echo "$flag" $OPTIND $OPTARG
   case "$flag" in
          g) VNC_GEOM=$OPTARG; echo "Requested VNC geometry: $VNC_GEOM";;
          d) VNC_DISP=$OPTARG; echo "Requested VNC display:  $VNC_DISP";;
          n) VNC_NAME=$OPTARG; echo "Requested VNC name:     $VNC_NAME";;
          h) echo "Usage: $VNC_SCRIPT  [-g <Vnc_WidthxHeight>] [-d <Vnc_Display_Nb>] [-n <Vnc_Name>] [-h] [-v]";
             exit;;
          v) echo $VNC_SCRIPT_VERSION;
             exit;;
   esac
done
echo ""

echo $VNC_SCRIPT_VERSION
echo ""

echo "Current modules loaded:"
echo "Executing: module list"
module list
echo ""

echo "Current shell limits:"
echo "Executing: ulimit -a"
ulimit -a
echo ""

# Vncserver Tuning
# The TurboVNC Server can use multiple threads to perform image encoding and compression: 
# NOTE: It will almost certainly have no effect on networks slower than 100 Megabit Ethernet
export TVNC_MT=1
export TVNC_NTHREADS=2

echo -e "Starting now the VNC server; executing:\n"
if [[ $VNC_DISP ]] ; then
   echo -e "\t vncserver -geometry $VNC_GEOM -name $VNC_NAME :$VNC_DISP"
               vncserver -geometry $VNC_GEOM -name $VNC_NAME :$VNC_DISP & 
else
   echo -e "\t vncserver -geometry $VNC_GEOM -name $VNC_NAME"
               vncserver -geometry $VNC_GEOM -name $VNC_NAME & 
fi
echo ""

echo "On which node it executes:"
echo -e    "\t$SLURM_JOB_NODELIST"
echo ""

sleep 5
VNC_DISPLAY=`/bin/ps -eo user,cmd | grep Xvnc | egrep "^$USER" | grep -v grep | awk '{print $3}'`
echo "Display assigned to your VNC session:"
echo -e    "\tnb VNC_DISPLAY=$VNC_DISPLAY "
echo ""

echo "How to check VNC node allocation:"
echo "	squeue -l -u $USER"
echo ""

echo "How to kill the VNC job:"
echo "  ssh $HOSTNAME vncserver -kill $VNC_DISPLAY"
echo "	scancel <VNC 'JOBID'>"
echo ""

echo "How to start a TurboVNC viewer on a Linux client (example):"
echo "	/opt/TurboVNC/bin/vncviewer $HOSTNAME$VNC_DISPLAY"
echo ""

#
# ADJUST THIS VALUE EXPRESSED IN SECONDS TO MATCH YOUR
# WALLTIME REQUESTED in --time=HH:MM:SS
#10 DAYS = 864000 seconds 
# 5 DAYS = 432000 seconds
# 2 DAYS = 172800 seconds
# 1 DAY = 86400 seconds,
sleep 864000 
#======END===============================================
