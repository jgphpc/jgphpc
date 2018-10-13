#!/bin/bash

#  piccinal@greina0:~ $ ./slurmjg.sh
#             cn=            cpu=            gpu=
#           cirra         haswell             k80
#         greina1       broadwell             k80
#        greina10       broadwell             k80
#        greina11               x               x
#        greina12               x               x
#        greina13               x               x
#        greina14         haswell             k80
#        greina15         haswell             k80
#        greina16               x               x
#        greina17       ivybridge             k20
#        greina18       ivybridge             k20
#        greina19       ivybridge             k20
#         greina2       broadwell             k80
#        greina20       ivybridge             k20
#        greina21       ivybridge             k20
#        greina22       broadwell               x
#        greina23       broadwell               x
#         greina3         haswell             k80
#         greina4         haswell             k80
#         greina5       broadwell             k80
#         greina6       broadwell             k80
#         greina7               x               x
#         greina8       broadwell               x
#         greina9         haswell             k40
#          node10               x               x
#          node11               x               x
#          node12               x               x
#          node13               x               x
#           node3               x               x
#           orion       ivybridge             k20

cpus="broadwell haswell ivybridge"
gpus="k80 k40 k20"
nodes=`scontrol show nodes |grep NodeName |awk '{print $1}' |cut -d= -f2 |sort -u`

printf "%15s %15s %15s\n" cn= cpu= gpu=
for i in $nodes; do
        cnsinfo=`sinfo -No "%N %P" -hn $i`
        for c in $cpus; do
                echo $cnsinfo |grep -q $c;rc=$?
                if [ "$rc" = 0 ]; then cpu=$c ;break;else cpu=x ;fi
        done
        for g in $gpus; do
                echo $cnsinfo |grep -q $g;rc=$?
                if [ "$rc" = 0 ]; then gpu=$g ;break;else gpu=x ;fi
        done
        printf "%15s %15s %15s\n" $i $cpu $gpu
done


