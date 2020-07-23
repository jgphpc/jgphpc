ARCH=
# module load daint-$ARCH
# #module 	rm craype-haswell
# #module	load craype-broadwell
# module	use /apps/dom/UES/jenkins/7.0.UP00/gpu/easybuild/modules/all
# module	use /apps/dom/UES/jenkins/7.0.UP00/gpu/easybuild/tools/modules/all
# module load /apps/common/UES/easybuild/modules/all/EasyBuild/latest

EEE=/Users/piccinal/git/production.git
export EASYBUILD_EXTERNAL_MODULES_METADATA=$EEE/easybuild/cray_external_modules_metadata.cfg
export EASYBUILD_INCLUDE_EASYBLOCKS=$EEE/easybuild/easyblocks/*.py
export EASYBUILD_ROBOT_PATHS=$EEE/easybuild/easyconfigs
export XDG_CONFIG_DIRS=$EEE/easybuild

# CCC=/apps/common/UES/jenkins/easybuild/software/EasyBuild-custom/cscs
# export EBDEVELEASYBUILDMINCUSTOM=$CCC/easybuild/EasyBuild-custom-cscs-easybuild-devel
# export EBROOTEASYBUILDMINCUSTOM=$CCC
# export EBVERSIONEASYBUILDMINCUSTOM=cscs

export EASYBUILD_MODULES_TOOL=Lmod # EnvironmentModulesC
# if [ $ARCH = "gpu" ] ;then
#     export EASYBUILD_OPTARCH=haswell
# else
#     export EASYBUILD_OPTARCH=broadwell
# fi
export EASYBUILD_RECURSIVE_MODULE_UNLOAD=0
export LC_ALL=C

TTT=/tmp/eb_tmp_delete # /dev/shm/piccinal
export EASYBUILD_BUILDPATH=$TTT/easybuild.jg/build/$ARCH
export EASYBUILD_TMPDIR=$TTT/easybuild.jg/$ARCH/tmp
# export XDG_RUNTIME_DIR=$SCRATCH/easybuild.jg/run/$ARCH

III=/Applications/CSCS/easybuild
export EASYBUILD_PREFIX=$III
export EASYBUILD_INSTALLPATH=$III
module use $III/modules/all
module load EasyBuild/3.9.0
export CC=gcc-9 
export CXX=g++-9
# echo $III/modules/all
# module use /apps/dom/UES/sandbox/piccinal/7.0.UP00/$ARCH/easybuild/modules/all
