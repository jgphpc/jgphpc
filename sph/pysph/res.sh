#!/bin/bash

# for in in effo_pysph.* ;do ~/jgphpc.git/sph/pysph/res.sh $in ;done
#
# effo_pysph.1.1.1.1.1.htno-dom.cube@1@1@@1@1@1@1@1@7.7.3@10077696@520.53344
# effo_pysph.1.1.10.10.1.htno-dom.cube@1@10@@1@1@10@10@1@7.7.3@10077696@65.16411
# effo_pysph.1.1.12.12.1.htno-dom.cube@1@12@@1@1@12@12@1@7.7.3@10077696@90.95830
# effo_pysph.1.1.2.2.1.htno-dom.cube@1@2@@1@1@2@2@1@7.7.3@10077696@264.45457
# effo_pysph.1.1.3.3.1.htno-dom.cube@1@3@@1@1@3@3@1@7.7.3@10077696@188.64729
# effo_pysph.1.1.4.4.1.htno-dom.cube@1@4@@1@1@4@4@1@7.7.3@10077696@146.35799
# effo_pysph.1.1.5.5.1.htno-dom.cube@1@5@@1@1@5@5@1@7.7.3@10077696@123.38301
# effo_pysph.1.1.6.6.1.htno-dom.cube@1@6@@1@1@6@6@1@7.7.3@10077696@104.29424
# effo_pysph.1.1.8.8.1.htno-dom.cube@1@8@@1@1@8@8@1@7.7.3@10077696@98.82138
# effo_pysph.10.10.1.1.1.htno-dom.cube@10@1@@10@10@1@1@1@7.7.3@10077696@67.8668
# effo_pysph.12.12.1.1.1.htno-dom.cube@12@1@@12@12@1@1@1@7.7.3@10077696@58.0589
# effo_pysph.2.2.1.1.1.htno-dom.cube@2@1@@2@2@1@1@1@7.7.3@10077696@277.578
# effo_pysph.2.2.2.2.1.htno-dom.cube@2@2@@2@2@2@2@1@7.7.3@10077696@158.474
# effo_pysph.2.2.3.3.1.htno-dom.cube@2@3@@2@2@3@3@1@7.7.3@10077696@114.499
# effo_pysph.2.2.4.4.1.htno-dom.cube@2@4@@2@2@4@4@1@7.7.3@10077696@89.5278
# effo_pysph.2.2.5.5.1.htno-dom.cube@2@5@@2@2@5@5@1@7.7.3@10077696@74.6465
# effo_pysph.2.2.6.6.1.htno-dom.cube@2@6@@2@2@6@6@1@7.7.3@10077696@65.9861
# effo_pysph.3.3.1.1.1.htno-dom.cube@3@1@@3@3@1@1@1@7.7.3@10077696@197.813
# effo_pysph.3.3.2.2.1.htno-dom.cube@3@2@@3@3@2@2@1@7.7.3@10077696@112.745
# effo_pysph.3.3.3.3.1.htno-dom.cube@3@3@@3@3@3@3@1@7.7.3@10077696@79.7831
# effo_pysph.3.3.4.4.1.htno-dom.cube@3@4@@3@3@4@4@1@7.7.3@10077696@63.6561
# effo_pysph.4.4.1.1.1.htno-dom.cube@4@1@@4@4@1@1@1@7.7.3@10077696@153.286
# effo_pysph.4.4.2.2.1.htno-dom.cube@4@2@@4@4@2@2@1@7.7.3@10077696@86.8447
# effo_pysph.4.4.3.3.1.htno-dom.cube@4@3@@4@4@3@3@1@7.7.3@10077696@61.5998
# effo_pysph.5.5.1.1.1.htno-dom.cube@5@1@@5@5@1@1@1@7.7.3@10077696@135.097
# effo_pysph.5.5.2.2.1.htno-dom.cube@5@2@@5@5@2@2@1@7.7.3@10077696@73.4511
# effo_pysph.6.6.1.1.1.htno-dom.cube@6@1@@6@6@1@1@1@7.7.3@10077696@111.076
# effo_pysph.6.6.2.2.1.htno-dom.cube@6@2@@6@6@2@2@1@7.7.3@10077696@60.281
# effo_pysph.7.7.1.1.1.htno-dom.cube@7@1@@7@7@1@1@1@7.7.3@10077696@97.8981
# effo_pysph.8.8.1.1.1.htno-dom.cube@8@1@@8@8@1@1@1@7.7.3@10077696@84.9232
# effo_pysph.9.9.1.1.1.htno-dom.cube@9@1@@9@9@1@1@1@7.7.3@10077696@77.1899

in=$1
dos2unix -q $in

nmpi=`echo $in |cut -d. -f2`
nomp=`echo $in |cut -d. -f4`
ntasks=`expr $nmpi \* $nomp`

slurm_nmpi=`grep "SLURM_NTASKS =" $in |awk '{print $4}'`
slurm_mpipercn=`grep "SLURM_NTASKS_PER_NODE =" $in |awk '{print $4}'`
slurm_nomp=`grep "SLURM_CPUS_PER_TASK =" $in |awk '{print $4}'`
slurm_nomp2=`grep "OMP_NUM_THREADS =" $in |awk '{print $4}'`
slurm_nht=`grep "SLURM_NTASKS_PER_CORE =" $in |awk '{print $4}'`
mpichv=`grep "CRAY MPICH version" $in |awk '{print $7}'`

nparticles=`grep "Number of particles:" $in |awk '{print $4}'`

if [ $nmpi -gt 1 ] ;then
    seconds=`grep  "Run took" $in |awk '{s=s+$5}END{print s/NR}'`
else
    seconds=`grep "^Run took" $in |awk '{print $3}'`
fi

# TODO: Setup took...

echo $in@$nmpi@$nomp@$ntasks\
@$seconds\
@$slurm_nmpi@$slurm_mpipercn\
@$slurm_nomp@$slurm_nomp2\
@$slurm_nht\
@$mpichv\
@$nparticles

# echo $in $nmpi $nomp : \
#     $slurm_nmpi $slurm_mpipercn \
#     $slurm_nomp $slurm_nomp2 \
#     $slurm_nht : \
#     $mpichv : $nparticles \
#     $seconds 
