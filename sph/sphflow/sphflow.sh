#!/bin/bash --noprofile

# ~/o/sphynx2.ods

in=$1

function sum()
{
    grep "$1" $in \
        |awk '{print $'$2'}' \
        |awk '{s=s+$0}END{printf "%.2f\n",s}'
}

# --- for i in o_* ;do ~/linux.git/sph/sphflow.sh $i ;done |snk 1
nparticles=`grep 'Total particle number' $in |cut -d: -f2 |tr -d " "`
nmpi=`grep 'SPH-flow is using' $in |awk '{printf "%04d",$4}'`
t_domain=`          sum 'Domain_decomposition' 3`
t_rk=`              sum 'timing: SSPRK' 4`
t_updating=`        sum 'Particle_Updating' 4`
t_process_neighbor=`sum 'Process Neighbors' 5`
t_neighbor_search=` sum 'Neighbor Search' 5`
t_real=`grep ^real $in |awk '{print $2}'`
t_total=`grep 'Total Elapsed time:' $in |awk '{printf "%.3f",$4}'`
nsteps=`grep 'Time Step' $in |wc -l`

echo "$nmpi $t_total $t_real $t_domain $t_rk $t_updating $t_process_neighbor $t_neighbor_search $nparticles $nsteps # $in"


exit 0

| 1 | 1.0/1.0 | 100.0% |    758.6 |
| 2 | 1.8/2.0 |  90.0% |    414.6 |
| 2.5 | 2.5/2.5 | 100.0% |    308.2 |
| 3 | 2.6/3.0 |  86.7% |    288.1 |
| 4 | 3.2/4.0 |  80.0% |    234.9 |
| 5 | 3.5/5.0 |  70.0% |    214.5 |
| 7.5 | 4.4/7.5 |  58.7% |    173.2 |
| 10 | 5.1/10.0 |  51.0% |    150.0 |
| 15 | 6.6/15.0 |  44.0% |    114.5 |
| 20 | 6.1/20.0 |  30.5% |    124.7 |
