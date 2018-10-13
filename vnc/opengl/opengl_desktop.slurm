#!/bin/bash -l
#SBATCH --job-name=vncdesktop
#SBATCH --output=vncdesktop.out
#SBATCH --nodes=1
#SBATCH -t 02:10:00
#SBATCH --gres=gpu:1
#SBATCH -C startx,gpu
##SBATCH -C startx,gpu
##SBATCH --account=usup

module load eglibs # /apps/daint/system/opt/nvidia/375.20/lib64/libOpenGL.so

if [ \! -e $HOME/.vnc/passwd ] ; then
	echo "For your protection, please run 'vncpasswd' before using vnc"
	exit 1
fi

i=`scontrol show hostname $SLURM_JOB_NODELIST`
PORT=1$(echo $i|awk -Fnid0 '{print $2}')
HOSTNAME=$(hostname)
RHOST=$(cat /etc/xthostname)101

### #RHOST=$(ssh -o "StrictHostKeyChecking no" -f login hostname)

echo "VNC Server accepting connections on ela:$PORT"
echo "On client machine:"
echo "ssh -f -L $PORT:${i}.${RHOST}:5901 $USER@ela.cscs.ch sleep 3600"
# echo "ssh -f -L $PORT:localhost:$PORT $USER@ela.cscs.ch ssh -L $PORT:localhost:$PORT $RHOST sleep 1200"
echo "/Applications/CSCS/TigerVNC Viewer 1.6.0.app/Contents/MacOS/TigerVNC Viewer => localhost:$PORT"
sync

#srun -n 1 startvncdesktop 1024x768
# ssh $i /apps/dom/system/bin/startvncdesktop 1280x720
ssh -o "StrictHostKeyChecking no" $i /apps/dom/system/bin/startvncdesktop 1920x1080
#srun -n 1 startvncdesktop 1920x1080

### #sets up tunnel from external login to internal nid
### ssh -o "StrictHostKeyChecking no" -f -N -R $PORT:$HOSTNAME:5901 $RHOST &> /dev/null

