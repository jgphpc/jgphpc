#!/bin/sh
#
# ./0_job_sizes.sh s398 2013-04-01 2013-07-01 $uid ; echo
# ./0_job_sizes.sh s398 2013-07-01 2013-10-01 $uid ; echo
#gid="s318"
gid=$1

mysql="mysql -h db.cscs.ch -uuseradm -preadonly stat_csmon"
#begin=2012-04-01
#begin=2013-04-01
#begin=2013-04-01
#end=2013-10-01
#end=2014-04-01

begin=$2
end=$3

username=$4


# begin=2012-04-01
# end=2012-11-15

# begin=2011-04-01
# end=2012-04-01

if [ ! -z $username ] ; then
        loop=`$mysql -s -E -e "select job_cpu_count from stat_csmon.job_accounting where group_id=\"$gid\" and facility=\"ROSA\" and job_endtime>\"$begin\" and job_endtime<=\"$end\" and username=\"$username\""`
else
        loop=`$mysql -s -E -e "select job_cpu_count from stat_csmon.job_accounting where group_id=\"$gid\" and facility=\"ROSA\" and job_endtime>\"$begin\" and job_endtime<=\"$end\""`
fi

jobsizes=`echo "$loop" | grep job_cpu_count|cut -d: -f2 | sort -u`
#echo "$loop"
jobsizes2=`echo $jobsizes |tr " " "\n"|sort -nk 1 |tr "\n" " "`
jobsizesn=`echo "$jobsizes" |wc -l`
echo $jobsizesn jobsizes = $jobsizes2 
#read
#exit 0

for jsize in $jobsizes2 ;do
        #echo -e "\n===> Query result for jobsize $jsize <==="
        s=`$mysql -s -E -e "select sum(job_walltime) from stat_csmon.job_accounting where group_id=\"$gid\" and facility=\"ROSA\" and job_endtime>\"$begin\" and job_endtime<=\"$end\" and job_cpu_count='"$jsize"'" |grep sum` #|cut -d: -f2`
        echo $jsize @ $s
#select * from job_accounting where job_id like '"$jsize"%'"
done > .eff

total=`awk '{s=s+$4}END{print s}' .eff`
awk -v tot=$total '{printf "%40s %.2f %%\n",$0,$4/tot*100}' .eff |sort -nk 5
echo "period = [ $begin : $end ] $username"
exit 0

# by hand :
# mysql> select sum(job_walltime) from stat_csmon.job_accounting where group_id="s208" and facility="ROSAXT5" and job_endtime>"2011-04-01" and job_endtime<="2011-12-01" and job_cpu_count="12" ;
