#!/bin/bash

# dos2unix !!!!

# Table 1:  Inclusive and Exclusive Time in Loops (from -hprofile_generate)
#    2      3           4           5           6           7       8           9
#   Loop | Loop Incl |     Time |  Loop Hit |      Loop |  Loop |      Loop | Function=/.LOOP[.]
#   Incl |      Time |    (Loop |           | Trips Avg | Trips | Trips Max |  PE=HIDE
#  Time% |           |    Adj.) |           |           |   Min |           |
# |-----------------------------------------------------------------------------
# | 98.0% | 10.094033 | 0.312042 |         1 |       4.0 |     4 |         4 | sphflow_.LOOP.2.li.340

# grep -A8 sphflow_.LOOP /project/c16/sphflow/dambreak/weak/loops/* |cut -d\| -f9|sort |uniq
#  getinteractionlist$interaction_lists_morton_mod_.LOOP.1.li.468
#  getneighborcells_step$octants_t_mod_.LOOP.1.li.889
#  getneighborcells_step$octants_t_mod_.LOOP.2.li.891
#  getneighborcells_step$octants_t_mod_.LOOP.3.li.893
#  interaction_muscl_renorm$interaction_muscl_renorm_mod_.LOOP.1.li.70
#  interaction_muscl_renorm$interaction_muscl_renorm_mod_.LOOP.2.li.71
#  interaction_tvr_fluid$interaction_tvr_fluid_mod_.LOOP.1.li.170 ---> Interactions/Interaction_TVR_Fluid_Riemann.F90
#  interaction_tvr_fluid$interaction_tvr_fluid_mod_.LOOP.2.li.171
#  radixsort_template_name$streamcompaction1_mod_.LOOP.2.li.164
#  radixsort_template_name$streamcompaction1_mod_.LOOP.3.li.180
#  sphflow_.LOOP.2.li.340

in=$1
loopname=$2
line=`grep "$2" $in`
# line=`grep interaction_lists_morton_mod_.LOOP.1.li.468 $in`

loop_timep=`echo $line |awk -F\| '{print $2}' |tr -d " "`
loop_time=`echo $line |awk -F\| '{print $3}' |tr -d " "`
loop_hit=`echo $line |awk -F\| '{print $5}' |tr -d " "`
loop_trip_min=`echo $line |awk -F\| '{print $7}' |tr -d " "`
loop_trip_avg=`echo $line |awk -F\| '{print $6}' |tr -d " "`
loop_trip_max=`echo $line |awk -F\| '{print $8}' |tr -d " "`

if [ -z $loop_timep ]    ;then loop_timep=x ; fi
if [ -z $loop_time ]     ;then loop_time=x ; fi
if [ -z $loop_hit ]      ;then loop_hit=x ; fi
if [ -z $loop_trip_min ] ;then loop_trip_min=x ; fi
if [ -z $loop_trip_avg ] ;then loop_trip_avg=x ; fi
if [ -z $loop_trip_max ] ;then loop_trip_max=x ; fi

echo $loop_timep $loop_time $loop_hit $loop_trip_min $loop_trip_avg $loop_trip_max \# $in
#$line

