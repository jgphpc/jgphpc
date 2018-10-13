#!/bin/bash --noprofile

# => ~/o/sphflow/resultsjg/sphflow_scaling.ods

#	 hyperbolic time step     [s]:   0.428575E-03
#	Time Step                 [s]:   0.428575E-03
#	 timing: Domain_decomposition:   0.214337E+00
#	 timing: Particle_Updating   :   0.180311E-01
#	 timing: Process Neighbors   :   0.210729E-01
#	 timing: Neighbor Search     :   0.133529E+00
#	Runge-Kutta4 step 1
#	# t_rk4_muscl:  2.0907E-01
#	# t_rk4_riemann:  2.4687E-01
#	Runge-Kutta4 step 2
#	# t_rk4_muscl:  2.0549E-01
#	# t_rk4_riemann:  2.4705E-01
#	Runge-Kutta4 step 3
#	# t_rk4_muscl:  2.0760E-01
#	# t_rk4_riemann:  2.4780E-01
#	Runge-Kutta4 step 4
#	# t_rk4_muscl:  2.0758E-01
#	# t_rk4_riemann:  2.4693E-01
#	 timing: RK41,RK42,RK44,RK44 :   6.9077E-01  5.2369E-01  5.3131E-01  5.2697E-01
#	 timing: RK4                 :   0.233712E+01
#	 timing: io                  :   0.419750E-01

# ------------------
#	*  MUSCL :call InteractionLoopOverParticles du fichier TVR.F90 l. 375
#	* Riemann solver : call InteractionLoopOverParticles du fichier TVR.F90 l. 629
#	* time step : call Time_Step du fichier SphFlow.f90 l. 380
#	* EOS : EOS_Sound_Speed du fichier Interaction_TVR_Fluid_Riemann.F90 l. 1475 et 1474
#	* output : call Output_Writing du fichier SphFlow.f90 l. 439
#	+ Runge Kutta 4 (la gearbox utilisait SSPRK) et Neighbor Search


in=$1
# dos2unix !!!!!!!!
dos2unix $in &> /dev/null

function sum()
{
    grep "$1" $in \
        |awk '{print $'$2'}' \
        |awk '{s=s+$0}END{printf "%.2f\n",s}'
}

function sum_muscl()
{
    grep -A2 "$1" $in \
        |grep 't_rk4_muscl' \
        |awk '{print $'$2'}' \
        |awk '{s=s+$0}END{printf "%.2f\n",s}'
}

function sum_riemman()
{
    grep -A2 "$1" $in \
        |grep 't_rk4_riemann' \
        |awk '{print $'$2'}' \
        |awk '{s=s+$0}END{printf "%.2f\n",s}'
}

# --- for i in o_* ;do ~/linux.git/sph/sphflow.sh $i ;done |snk 1
nparticles=`grep 'Total particle number' $in |cut -d: -f2 |tr -d " "`
nmpi=`grep 'SPH-flow is using' $in |awk '{printf "%04d",$4}'`

# --- hyperbolic time step     [s]:   0.428575E-03
t_hyperbolic=`      sum 'hyperbolic time step' 5`

# --- Time Step                 [s]:   0.428575E-03
t_timestep=`        sum 'Time Step' 4`

# --- timing: Domain_decomposition:   0.214337E+00
t_domain=`          sum 'Domain_decomposition' 3`

# --- timing: Particle_Updating   :   0.180311E-01
t_updating=`        sum 'Particle_Updating' 4`

# --- timing: Process Neighbors   :   0.210729E-01
t_process_neighbor=`sum 'Process Neighbors' 5`

# --- timing: Neighbor Search     :   0.133529E+00
t_neighbor_search=` sum 'Neighbor Search' 5`


# --- timing: RK41,RK42,RK44,RK44 :   4.3200E-01  4.9916E-01  4.8865E-01  4.9270E-01
t_rk41=`            sum 'timing: RK41,RK42,RK44,RK44' 4`
t_rk42=`            sum 'timing: RK41,RK42,RK44,RK44' 5`
t_rk43=`            sum 'timing: RK41,RK42,RK44,RK44' 6`
t_rk44=`            sum 'timing: RK41,RK42,RK44,RK44' 7`

# --- Runge-Kutta4 step 1
#	# t_rk4_muscl:  2.0907E-01
#	# t_rk4_riemann:  2.4687E-01
t_rk41m=`sum_muscl   'Runge-Kutta4 step 1' 3`
t_rk41r=`sum_riemman 'Runge-Kutta4 step 1' 3`
t_rk42m=`sum_muscl   'Runge-Kutta4 step 2' 3`
t_rk42r=`sum_riemman 'Runge-Kutta4 step 2' 3`
t_rk43m=`sum_muscl   'Runge-Kutta4 step 3' 3`
t_rk43r=`sum_riemman 'Runge-Kutta4 step 3' 3`
t_rk44m=`sum_muscl   'Runge-Kutta4 step 4' 3`
t_rk44r=`sum_riemman 'Runge-Kutta4 step 4' 3`

# --- timing: RK4                 :   0.233712E+01
t_rk4=`              sum 'timing: RK4 ' 4`
## rot_square
## gearbox: t_rk=`              sum 'timing: SSPRK' 4`
## dambreak:

# --- timing: io                  :   0.419750E-01
t_io=`              sum 'timing: io ' 4`

# --- slurm
t_slurm=`grep JOBID $in |cut -d= -f2 |xargs sacct -o Elapsed,State -j |grep -m1 COMPLETED |awk '{print "~/linux.git/slurm/2seconds.sh",$0}'|sh|cut -d\# -f1`
# t_real=`grep ^real $in |awk '{print $2}'`   # /usr/bin/time -p

t_total=`grep 'Total Elapsed time:' $in |awk '{printf "%.3f",$4}'`
nsteps=`grep 'Time Step' $in |wc -l`
t_max=`grep ' nstep=' $in |tail -1 |awk '{printf "%.6f",$6}'`

echo  "$nmpi $t_slurm $t_total $nparticles $nsteps $t_max # $in "

echo "$t_hyperbolic "
echo "$t_timestep "
echo "$t_domain "
echo "$t_updating "
echo "$t_process_neighbor "
echo "$t_neighbor_search "
echo "$t_rk41 "
echo "$t_rk42 "
echo "$t_rk43 "
echo "$t_rk44 "
echo "$t_rk4 "
echo "$t_rk41m "
echo "$t_rk41r "
echo "$t_rk42m "
echo "$t_rk42r "
echo "$t_rk43m "
echo "$t_rk43r "
echo "$t_rk44m "
echo "$t_rk44r "
echo "$t_io "

# echo -n "$t_hyperbolic "
# echo -n "$t_timestep "
# echo -n "$t_domain "
# echo -n "$t_updating "
# echo -n "$t_process_neighbor "
# echo -n "$t_neighbor_search "
# echo -n "$t_rk41 $t_rk42 $t_rk43 $t_rk44 $t_rk4 "
# echo -n "$t_rk41m $t_rk41r "
# echo -n "$t_rk42m $t_rk42r "
# echo -n "$t_rk43m $t_rk43r "
# echo -n "$t_rk44m $t_rk44r "
# echo -n "$t_io "
# echo -n "$ "
# echo

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
