#!/bin/sh
# job size of all users

mysql="mysql -h db.cscs.ch -uuseradm -preadonly stat_csmon"
facility="DAINT"
begin[1]="2017-01-01"
begin[2]="2017-02-01" ; end[1]=${begin[2]}
begin[3]="2017-03-01" ; end[2]=${begin[3]}
begin[4]="2017-04-01" ; end[3]=${begin[4]}
begin[5]="2017-05-01" ; end[4]=${begin[5]}
begin[6]="2017-06-01" ; end[5]=${begin[6]}
begin[7]="2017-07-01" ; end[6]=${begin[7]}
begin[8]="2017-08-01" ; end[7]=${begin[8]}
begin[9]="2017-09-01" ; end[8]=${begin[9]}
begin[10]="2017-10-01" ; end[9]=${begin[10]}
begin[11]="2017-11-01" ; end[10]=${begin[11]}
begin[12]="2017-12-01" ; end[11]=${begin[12]}
# begin[3]="2017-05-01" ; end[2]=${begin[3]}
# begin[4]="2017-06-01" ; end[3]=${begin[4]}
#                         end[4]=`date +%Y-%m-%d`
#echo ${begin[1]} ${end[1]}
#echo ${begin[2]} ${end[2]}
#echo ${begin[3]} ${end[3]}
#echo ${begin[4]} ${end[4]}

  ####    ####   #
 #       #    #  #
  ####   #    #  #
      #  #  # #  #
 #    #  #   #   #
  ####    ### #  ######

function get_all_sizes() {

    facility=$1
    begin=$2
    $mysql -s -e "select job_cpu_count from stat_csmon.job_accounting where facility=\"$facility\" and job_endtime>=\"$begin\" and group_id!=\"csstaff\" group by job_cpu_count; "

}

function get_usage_by_bin() {

    min=$1
    max=$2
    facility=$3
    begin=$4
    end=$5
    $mysql -s -e "select sum(job_charge * job_cpu_count * TIME_TO_SEC(job_walltime)/3600.0) from job_accounting where facility=\"$facility\" and job_endtime>=\"$begin\" and job_endtime<\"$end\" and job_cpu_count>\"$min\" and job_cpu_count<=\"$max\" ;" |awk '{printf "%d",$0}'

}

function get_usage_by_month() {

    facility=$1
    begin=$2
    end=$3
    $mysql -s -e "select sum(job_charge * job_cpu_count * TIME_TO_SEC(job_walltime)/3600.0) from job_accounting where facility=\"$facility\" and job_endtime>=\"$begin\" and job_endtime<\"$end\" ;" |awk '{printf "%d",$0}'

}

# --- daint-gpu = 5320 cn (08/2017)
# --- daint-mc  = 1429 cn (08/2017)
#         total = 6749 cn (08/2017)           
# --- MaxNodes=2400cn * 12c/cn = 28800c
## grep 'compute   xt       CNL   24  12 ' eff.xtprocadmin-daintgpu |wc -l
## grep ActiveFeatures=mc eff.scn.res |awk -F"ActiveFeatures=" '{print $2}' |awk -F, '{print $1}' |sort |uniq -c
### 1405  mc *36c/cn = 50580c
### 5192 gpu *12c/cn = 62304c
### xxx cores split into 10 bins:
cores[1]=0     #cores[1]=0      #cores[1]=0
cores[2]=110   #cores[2]=2880   #cores[2]=6230
cores[3]=220   #cores[3]=5760   #cores[3]=12460
cores[4]=330   #cores[4]=8640   #cores[4]=18691
cores[5]=440   #cores[5]=11520  #cores[5]=24921
cores[6]=550   #cores[6]=14400  #cores[6]=31152
cores[7]=660   #cores[7]=17280  #cores[7]=37382
cores[8]=770   #cores[8]=20160  #cores[8]=43612
cores[9]=880   #cores[9]=23040  #cores[9]=49843
cores[10]=990  #cores[10]=25920 #cores[10]=56073
cores[11]=1100 #cores[11]=28800 #cores[11]=62304

# --- daint
echo 
echo 'CNH per month:'
echo -n "[YYYY-MM-01:YYYY-MM-01] |"
sm1=`expr ${#cores[@]} - 1`
for i in `seq 1 ${#cores[@]}` ; do
    ip1=`expr $i + 1`
    printf "%5s-%5s|" ${cores[$i]} ${cores[$ip1]}
done ; echo

for month in `seq 5`;do
    echo -n "[${begin[$month]}:${end[$month]}] |"
    for i in `seq 10` ;do
                ip1=`expr $i + 1`
                usage=`get_usage_by_bin ${cores[$i]} ${cores[$ip1]} $facility ${begin[$month]} ${end[$month]}`
                printf "%11s|" $usage
    done ; echo
done

# --- zoom in smaller jobs:
echo 
echo 'CNH per month (smaller jobs only):'
allsizes=`get_all_sizes $facility ${begin[1]}`
minjobsize=`echo "$allsizes" |head -1`
maxjobsize=`echo "$allsizes" |tail -1`
numjobsize=`echo "$allsizes" |uniq |wc -l` 

echo "$facility : numjobsize minjobsize maxjobsize (cores)"
echo "$facility : $numjobsize $minjobsize $maxjobsize cores"

unset $cores
for i in `seq 0 5` ;do
    ip1=`expr $i + 1`
    cores[$ip1]=`echo $i |awk -v c=$maxjobsize '{print int(c*$0/5)}'`
    # echo c$ip1=${cores[$ip1]}
done

echo -n "[YYYY-MM-01:YYYY-MM-01] |"
sm1=`expr ${#cores[@]} - 1`
for i in `seq 1 5` ; do
    ip1=`expr $i + 1`
    printf "%5s-%5s|" ${cores[$i]} ${cores[$ip1]}
done ; echo

for month in `seq 1 5`;do
    echo -n "[${begin[$month]}:${end[$month]}] |"
    # 
    for i in `seq 1 5` ;do
                ip1=`expr $i + 1`
                usage=`get_usage_by_bin ${cores[$i]} ${cores[$ip1]} $facility ${begin[$month]} ${end[$month]}`
                printf "%11s|" $usage
    done ; echo
done

# --- zoom in smaller jobs (%):
echo
echo 'CNH per month (%):'















echo -n "[YYYY-MM-01:YYYY-MM-01] |"
sm1=`expr ${#cores[@]} - 1`
for i in `seq 1 5` ; do
    ip1=`expr $i + 1`
    printf "%5s-%5s|" ${cores[$i]} ${cores[$ip1]}
done ; echo

for month in `seq 1 5`;do
    echo -n "[${begin[$month]}:${end[$month]}] |"
    usagemonth=`get_usage_by_month $facility ${begin[$month]} ${end[$month]}`
    for i in `seq 1 5` ;do
                ip1=`expr $i + 1`
                usage=`get_usage_by_bin ${cores[$i]} ${cores[$ip1]} $facility ${begin[$month]} ${end[$month]}`
                usagepercent=`echo $usage $usagemonth |awk '{printf "%d\n",$1/$2*100}'`
                printf "%10s%%|" $usagepercent
    done ; echo " $usagemonth"
done


# for month in `seq 1 ${#begin[@]}` ; do
#         for i in `seq 1 $sm1` ; do
# 
#                 ip1=`expr $i + 1`
#                 usage=`get_usage_by_bin ${cores[$i]} ${cores[$ip1]} $facility ${begin[$month]} ${end[$month]}`
#                 printf "%11s|" $usage
#                 #echo "$facility : numjobsize=$numjobsize minjobsize=$minjobsize maxjobsize=$maxjobsize : ${cores[$i]} ${cores[$ip1]} cores : $usage"
#         done ; echo
# done

exit 0



CNH per month:
[YYYY-MM-01:YYYY-MM-01] |    0- 6230| 6230-12460|12460-18691|18691-24921|24921-31152|31152-37382|37382-43612|43612-49843|49843-56073|56073-62304|62304-     |
[2017-01-01:2017-02-01] |    2969207|          0|          0|          0|          0|          0|          0|          0|          0|          0|
[2017-02-01:2017-03-01] |    3354995|          0|          0|          0|          0|          0|          0|          0|          0|          0|
[2017-03-01:2017-04-01] |    4325743|          0|          0|          0|          0|          0|          0|          0|          0|          0|
[2017-04-01:2017-05-01] |    2976456|          0|          0|          0|          0|          0|          0|          0|          0|          0|
[2017-05-01:2017-06-01] |     382632|          0|          0|          0|          0|          0|          0|          0|          0|          0|

CNH per month (smaller jobs only):
DAINT : numjobsize minjobsize maxjobsize (cores)
DAINT : 297 1 5320 cores
[YYYY-MM-01:YYYY-MM-01] |    0- 1064| 1064- 2128| 2128- 3192| 3192- 4256| 4256- 5320|
[2017-01-01:2017-02-01] |    2939747|      24570|        781|          0|       4108|
[2017-02-01:2017-03-01] |    3336188|      16934|       1872|          0|          0|
[2017-03-01:2017-04-01] |    3995447|     258991|      42431|       2957|      25916|
[2017-04-01:2017-05-01] |    2555149|     236608|       2322|       1361|     181014|
[2017-05-01:2017-06-01] |     369316|       4940|        801|         20|       7525|

CNH per month (%):
[YYYY-MM-01:YYYY-MM-01] |    0- 1064| 1064- 2128| 2128- 3192| 3192- 4256| 4256- 5320|
[2017-01-01:2017-02-01] |        99%|         0%|         0%|         0%|         0%| 2969207
[2017-02-01:2017-03-01] |        99%|         0%|         0%|         0%|         0%| 3354995
[2017-03-01:2017-04-01] |        92%|         5%|         0%|         0%|         0%| 4325743
[2017-04-01:2017-05-01] |        85%|         7%|         0%|         0%|         6%| 2976456
[2017-05-01:2017-06-01] |        96%|         1%|         0%|         0%|         1%| 382632















bins=5
bin[0]=1
for i in `seq 1 $bins`;do
        bin[$i]=`echo $minjobsize $maxjobsize $bins $i |awk '{printf "%d",($2-$1)/$3*$4}'`
        im1=`expr $i - 1`
        usage=`get_usage_by_bin ${bin[$im1]} ${bin[$i]} $facility $begin`
        echo "$facility : numjobsize=$numjobsize minjobsize=$minjobsize maxjobsize=$maxjobsize :  ${bin[$im1]} ${bin[$i]} : $usage"
done
#echo ${bin[*]}

exit 0








loop=`$mysql -s -E -e "select job_cpu_count from stat_csmon.job_accounting where group_id=\"$gid\" and facility=\"ROSA\" and job_endtime>\"$begin\" and job_endtime<=\"$end\""`

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

exit 0

# select partition from stat_csmon.job_accounting where facility="DAINT" and job_endtime>="2017-05-1" group by partition;
+-----------+
| partition |
+-----------+
| debug     |
| jalet     |
| low       |
| normal    |
| prepost   |
| total     |

# by hand :
# mysql> select sum(job_walltime) from stat_csmon.job_accounting where group_id="s208" and facility="ROSAXT5" and job_endtime>"2011-04-01" and job_endtime<="2011-12-01" and job_cpu_count="12" ;
