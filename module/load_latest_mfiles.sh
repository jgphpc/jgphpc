#!/bin/bash

source $MODULESHOME/init/bash
loadedmf=`module list -t 2>&1 |grep -v Modulefiles:`
export MODULEPATH=/opt/cray/craype/default/modulefiles:/opt/cray/ari/modulefiles:/opt/cray/modulefiles:/opt/modulefiles

#set -x
for i in $loadedmf ; do
#for i in cce/8.3.12; do
        
        modulename=`echo $i |cut -d/ -f1`
        loadedmfV=`echo $i |cut -d/ -f2`
        latestmfV=`module avail -t $modulename 2>&1 |grep ${modulename}/ |sed "s-(default)--g" |cut -d/ -f2 |sort -nk1 |tail -1`
        if [ "$loadedmfV" != "$latestmfV" ] ; then
                echo module swap $modulename/$loadedmfV         $modulename/$latestmfV
        #else
        #        echo $modulename xxx $loadedmfV === $latestmfV
        fi

done
