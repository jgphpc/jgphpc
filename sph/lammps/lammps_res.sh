#!/bin/bash --noprofile

# --- for i in LAMMPS_*_strong/PrgEnv-gnu/LAMMPS_*_strong.out ;do ~/linux.git/sph/lammps/lammps_res.sh $i ;done |snk 1
# Loop time of 317.506 on 1 procs for 40000 steps with 15702 atoms

in=$1
# dos2unix !!!!!!!!
### dos2unix $in &> /dev/null

function sum()
{
    grep "$1" $in \
        |awk '{print $'$2'}' \
        |awk '{s=s+$0}END{printf "%.2f\n",s}'
}

nmpi=$1
echo -n "steps@"
for steps in 1000 5000 10000 20000 30000 40000 ;do 
    echo -n "$steps@"
done ;echo

for g in Pair Neigh Comm Output Modify Other;do 
    echo -n "$g@"
    for steps in 1000 5000 10000 20000 30000 40000 ;do 
        t=`grep "^$g " LAMMPS_${nmpi}_${steps}_010000wp_strong.out |awk -F\| '{print $6}'`;
        echo -n "$t@";
    done;
    echo;
done

exit 0


# Loop time of 109.324 on 4 procs for 30000 steps with 16000 atoms
timeline=`grep "^Loop time of" $in`
t_loops=`echo "$timeline" |awk '{print $4}'`
nmpi=`echo "$timeline" |awk '{printf "%04d",$6}'`
nsteps=`echo "$timeline" |awk '{print $9}'`
nparticles=`echo "$timeline" |awk '{print $12}'`
nparticlesBC=`grep 'atoms in group bc' $in |awk '{print $1}'`
nparticlesWATER=`grep 'atoms in group water' $in |awk '{print $1}'`

# --- slurm
#t_slurm=`grep JOBID $in |cut -d= -f2 |xargs sacct -o Elapsed,State -j |grep -m1 COMPLETED |awk '{print "~/linux.git/slurm/2seconds.sh",$0}'|sh|cut -d\# -f1`
#t_total=`grep 'Total Elapsed time:' $in |awk '{printf "%.3f",$4}'`
#t_max=`grep ' nstep=' $in |tail -1 |awk '{printf "%.6f",$6}'`
#echo  "$nmpi $t_slurm $t_total $nparticles $nsteps $t_max # $in "
echo  "$nmpi $t_loops $nsteps $nparticles $nparticlesBC $nparticlesWATER # $in "

exit 0

