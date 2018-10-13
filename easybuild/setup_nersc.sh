#!/usr/local/bin/bash

PROJ=/global/homes/p/piccinal/DELETE/ebjg
# export PROJ=${1}
export EASYBUILD_REPOSITORYPATH=$PROJ/easybuild/ebfiles_repo/
export EASYBUILD_REPOSITORY=FileRepository
type module ; echo MODULESHOME = $MODULESHOME
# 
# # Switch environment modules (set PATH varible)
# echo "Switching to environment modules ..."
# if [[ "$hostName" == "daint" || "$hostName" == "dora" || "$hostName" == "santis" ]] ; then
#     source /opt/modules/3.2.10.3/init/bash
#     export PATH=/opt/modules/3.2.10.3/bin/:$PATH
# elif [[ "$hostName" == "brisi" ]] ; then
#     source /opt/cray/pe/modules/3.2.10.4/init/bash
#     export PATH=/opt/cray/pe/modules/3.2.10.4/bin/:$PATH
#     export CRAY_CPU_TARGET=broadwell
# elif [[ "$hostName" == "eschaln-" || "$hostName" == "keschln-" ]] ; then
#     source /usr/Modules/3.2.10/init/bash
#     export PATH=/usr/Modules/3.2.10/bin/:$PATH
# elif [[ "$hostName" == "pilatus" ]] ; then
#     export PATH=/usr/share/Modules/tcl/:$PATH
#     source /usr/share/Modules/tcl/init/bash
# elif [[ "$hostName" == "monch" ]] ; then
#     export PATH=/apps/monch/modules/3.2.10/bin/:$PATH
#     source /apps/monch/modules/3.2.10/init/bash
# elif [[ "$hostName" == "castor" ]] ; then
#     export PATH=/apps/castor/Modules/3.2.10/bin/:$PATH
#     source /apps/castor/Modules/3.2.10/init/bash
# elif [[ "$hostName" == "ela" ]] ; then
#     export PATH=/usr/share/Modules/tcl/:$PATH
# fi

export EASYBUILD_MODULES_TOOL=EnvironmentModulesC
# export EASYBUILD_MODULES_TOOL=EnvironmentModulesTcl

export EASYBUILD_PREFIX=${PROJ}/easybuild
export EASYBUILD_SET_GID_BIT=1
export EASYBUILD_GROUP_WRITABLE_INSTALLDIR=1
#export EASYBUILD_STICKY_BIT=1
export EASYBUILD_UMASK=002
export EASYBUILD_BUILDPATH=/dev/shm/$USER
#export EASYBUILD_ROBOT_PATHS=/apps/common/easybuild/cscs_easyconfigs/:/apps/common/easybuild/ebfiles_repo/${hostName}:
# export EASYBUILD_ROBOT_PATHS=/apps/common/easybuild/cscs_easyconfigs/:
# export EASYBUILD_INCLUDE_EASYBLOCKS="/apps/common/easybuild/easyblocks/*.py"
export EASYBUILD_IGNORE_OSDEPS=0
# export EASYBUILD_HIDE_DEPS=Bison,Doxygen,JasPer,NASM,SQLite,Szip,Tcl,bzip2,cURL,flex,freetype,libjpeg-turbo,libpng,libreadline,libtool,libxml2,ncurses,zlib,M4,Serf,APR,APR-util,expat,SCons,binutils,Coreutils,GLib,Qt,SCOTCH,Tk,hwloc,libffi,libunwind,make,numactl,pkg-config,gettext,Autotools,Automake,Autoconf,GCCcore,OPARI2,OTF2,UDUNITS,ZeroMQ,OpenPGM,util-linux,libsodium,libQGLViewer,Eigen,GTS,GL2PS,PyGTS,PyQt,IPython,Python-Xlib,LOKI,SIP,NASM,PIL,libjpeg-turbo,libxcb,libX11,libXau,xproto,kbproto,inputproto,libpthread-stubs,xextproto,libXdmcp,xcb-proto,xtrans,LibTIFF,byacc,guile,libunistring,CMake,PCRE,XZ,PROJ
export EASYBUILD_RECURSIVE_MODULE_UNLOAD=1

# # Set up private repository for jenkins user (it doesnt belong to csstaff group, it is not supposed to write under /apps/common)
# if [[ -w /apps/common/easybuild/sources/ ]] ; then
#     export EASYBUILD_SOURCEPATH=/apps/common/easybuild/sources/
# elif [[ $USER == "jenscscs" ]] ; then
#     export EASYBUILD_SOURCEPATH=$HOME/sources #/scratch/jenscscs/sources/
# else
    export EASYBUILD_SOURCEPATH=$PROJ/sources #$HOME
    mkdir -p $EASYBUILD_SOURCEPATH
# fi

# if [[ "$hostName" == "daint" || "$hostName" == "dora" || "$hostName" == "santis" || "$hostName" == "brisi" ]] ; then
#     export EASYBUILD_EXTERNAL_MODULES_METADATA=/apps/common/easybuild/cray_external_modules_metadata.cfg
#     export EASYBUILD_OPTARCH=$CRAY_CPU_TARGET
#     export EASYBUILD_RECURSIVE_MODULE_UNLOAD=0 #recursive unload currently not working on Cray* toolchains
# fi

# /apps/common = custom cscs easyblocks
# export PYTHONPATH=$PYTHONPATH:/apps/common/gitpython/lib/python2.7/site-packages/
# env | grep EASYBUILD
echo PYTHONPATH=$PYTHONPATH |tr : "\n"
#echo PATH=$PATH

# echo "Updating \$MODULEPATH..."
#module use $EASYBUILD_PREFIX/modules/all
export MODULEPATH=$EASYBUILD_PREFIX/modules/all:$MODULEPATH
echo MODULEPATH=$MODULEPATH |tr : "\n"

# echo "Loading EasyBuild..."
# module load /apps/common/UES/easybuild/modules/all/EasyBuild/latest 
module use /global/homes/p/piccinal/DELETE/ebjg/modules/all
module load EasyBuild
eb --version 
