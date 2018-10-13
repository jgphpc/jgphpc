#!/bin/bash

# this is much simpler:
# scontrol show job --oneliner |grep Partition=debug |awk '{print $1}' |cut -d= -f2 |awk '{print "scontrol show job",$0}' |sh
# sinfo -p debug
# sinfo -s -p debug

tmpf=`basename $0`
mkdir -p /dev/shm/$USER
tmpfile1=/dev/shm/$USER/eff1.$tmpf
tmpfile2=/dev/shm/$USER/eff2.$tmpf
tmpfile3=/dev/shm/$USER/eff3.$tmpf
tmpfile2s=/dev/shm/$USER/eff2s.$tmpf
tmpfile3s=/dev/shm/$USER/eff3s.$tmpf
rm -f $tmpfile1 $tmpfile2 $tmpfile3 
rm -f $tmpfile2s $tmpfile3s

  ####      #    #    #  ######   ####
 #          #    ##   #  #       #    #
  ####      #    # #  #  #####   #    #
      #     #    #  # #  #       #    #
 #    #     #    #   ##  #       #    #
  ####      #    #    #  #        ####
# --- sinfo:
# PARTITION AVAIL JOB_SIZE  TIMELIMIT   CPUS  S:C:T   NODES STATE      NODELIST
# debug     up    1-4           30:00     72 2:18:2       3 allocated  nid000[09-11]

# --- is there any node allocated in the debug PARTITION ?
sinfo -p debug &> $tmpfile1
grep -q allocated $tmpfile1 ;rc=$?
# echo rc=$rc

# --- yes=allocated but what is the list of nodes = $tmpfile2 ?
if [ $rc -eq 0 ] ;then 

    allocatedcn_sinfo=`grep allocated $tmpfile1 |awk '{print $7}'`
    nodelist_sinfo=`grep allocated $tmpfile1 |awk '{print $9}'`
    # nid00[008-011,448-451]

        cnlist_sinfo=`echo $nodelist_sinfo |tail -1 |tr -d " " |cut -d[ -f2 |cut -d] -f1 |tr , " " |sed "s-nid--"`
        # PARTITION AVAIL JOB_SIZE  TIMELIMIT   CPUS  S:C:T   NODES STATE      NODELIST
        # debug     up    1-4           30:00     72 2:18:2       8 allocated  nid00[008-011,448-451]
        # nid00[008-011,448-451]
        # => 008-011 448-451
        for cnsublist in $cnlist_sinfo ;do

            first=`echo $cnsublist |cut -d- -f1`
            last=`echo $cnsublist |cut -d- -f2`
            # if [ -z $last ] ;then echo "#error sinfo last=$last" ;last=$first ;fi
            seq $first $last |awk '{printf "nid%05d\n", $0}' >> $tmpfile2
		    # nid04689
    		# nid04690
    		# nid04691
            
        done

fi

  ####     ##     ####    ####    #####
 #        #  #   #    #  #    #     #
  ####   #    #  #       #          #
      #  ######  #       #          #
 #    #  #    #  #    #  #    #     #
  ####   #    #   ####    ####      #
# --- list of running jobids:
if [ $rc -eq 0 ] ;then 
    jobids=`squeue --noheader -t RUNNING -o "%.6i"` # how to use &/coproc ?
    # http://unix.stackexchange.com/questions/86270/how-do-you-use-the-command-coproc-in-bash
    # http://stackoverflow.com/questions/20017805/bash-capture-output-of-command-run-in-background
fi

if [ $rc -eq 0 ] ;then 

    # --- what is the list of running nodes = $tmpfile3 ?
    for jid in $jobids ;do

        echo -n "."
        cnlist_R=`sacct -j $jid -o nodelist%1000 |tail -1 |tr -d " " |cut -d[ -f2 |cut -d] -f1 |tr , " " |sed "s-nid--"`
        # nid0[4648-4667,4672,4674-4675,4679,4681,4689,4694-4696,4704-4706,4708,4721-4751,4822-4827]
        # => 4648-4667 4672 4674-4675 4679 4681 4689 4694-4696 4704-4706 4708 4721-4751 4822-4827

        rm -f $tmpfile3
        for cnsublist in $cnlist_R ;do

            first=`echo $cnsublist |cut -d- -f1`
            last=`echo $cnsublist |cut -d- -f2`
            # if [ -z $last ] ;then echo "#error last=$last" ;last=$first ;fi
            seq $first $last |awk '{printf "nid%05d\n", $0}' >> $tmpfile3
		    # nid04689
    		# nid04690
    		# nid04691
            
        done  # cnsublist in $cnlist_R

         ####    ####   #    #  #####     ##    #####   ######
        #    #  #    #  ##  ##  #    #   #  #   #    #  #
        #       #    #  # ## #  #    #  #    #  #    #  #####
        #       #    #  #    #  #####   ######  #####   #
        #    #  #    #  #    #  #       #    #  #   #   #
         ####    ####   #    #  #       #    #  #    #  ######
        sort -nk1 $tmpfile2 > $tmpfile2s
        sort -nk1 $tmpfile3 > $tmpfile3s
        node_is_being_used=`comm -12 $tmpfile2s $tmpfile3s 2>&1`  # &> /dev/null
        if [ ! -z $node_is_being_used ] ;then
        # rc2=$?
        # if [ $rc2 != 0 ] ;then
            # echo "comparing jid=$jid with allocated nodes in debug partition"
            scontrol show job $jid
            sinfo -p debug
            echo
            # echo "continue ?"
            # read
        else
            echo -n "."
        fi

    done  # jid in $jobids

fi
# wait

exit 0

