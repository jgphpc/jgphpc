#!/bin/bash -l
#SBATCH --job-name=vncdesktop
#SBATCH --output=o_vncdesktop
#SBATCH --nodes=1
#SBATCH -t 00:10:00
#SBATCH --gres=gpu:1
#SBATCH -C startx
#SBATCH --account=usup
##SBATCH --exclude=nid00170, nid00190
##SBATCH --partition=viz

# module load viz/1.4
export          DISPLAY=:0
PATH=/apps/santis/Viz/Xorg-1.4/bin:$PATH
PATH=/apps/santis/Viz/VirtualGL-1.4/build/bin:$PATH
PATH=/apps/santis/Viz/VirtualGL-1.4/VirtualGL-2.3.3/bin:$PATH
export          PATH
LD_LIBRARY_PATH=/apps/santis/Viz/Xorg-1.4/lib:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=/apps/santis/Viz/VirtualGL-1.4/VirtualGL-2.3.3/lib:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=/opt/cray/nvidia/default/lib64:$LD_LIBRARY_PATH
export          LD_LIBRARY_PATH

if [ \! -e $HOME/.vnc/passwd ] ; then
	echo "For your protection, please run 'vncpasswd' before using vnc"
	exit 1
fi

HOSTNAME=$(hostname)
for i in `scontrol show hostname $SLURM_JOB_NODELIST` ;do
        PORT=1$(echo $i|awk -Fnid0 '{print $2}')
        for j in 0 1 2 3 ;do
                ssh -o "StrictHostKeyChecking no" -f -N -R $PORT:$i:5901 ela$j &> /dev/null
        done
done

echo "# ---------------------------------------------"
echo "# VNC Server accepting connections on ela:$PORT"
echo "# On client machine, run:"
echo "ssh -f -L $PORT:localhost:$PORT $USER@ela.cscs.ch sleep 120"
echo "vncviewer localhost:$PORT"
echo "when done, run: scancel  # vncserver -kill not needed"
echo "# ---------------------------------------------"

#aprun -n 1 startvncdesktop 1024x768
#aprun -n 1 startvncdesktop 1280x720
slurm_version=`sinfo -V |awk '{print $2}' |cut -d. -f1`
if [ "$slurm_version" = 14 ] ; then
        aprun -n 1 startvncdesktop 1920x1080
fi

if [ "$slurm_version" = 15 ] ; then
        srun -n 1 startvncdesktop 1920x1080
fi
