ARCH=mc
module load daint-$ARCH
# #module 	rm craype-haswell
# #module	load craype-broadwell
# module	use /apps/dom/UES/jenkins/7.0.UP00/gpu/easybuild/modules/all
# module	use /apps/dom/UES/jenkins/7.0.UP00/gpu/easybuild/tools/modules/all
module load /apps/common/UES/easybuild/modules/all/EasyBuild/latest

EEE=/apps/common/UES/sandbox/jgp/production.git
export EASYBUILD_EXTERNAL_MODULES_METADATA=$EEE/easybuild/cray_external_modules_metadata.cfg
export EASYBUILD_INCLUDE_EASYBLOCKS=$EEE/easybuild/easyblocks/*.py
export EASYBUILD_ROBOT_PATHS=$EEE/easybuild/easyconfigs
export XDG_CONFIG_DIRS=$EEE/easybuild

CCC=/apps/common/UES/jenkins/easybuild/software/EasyBuild-custom/cscs
export EBDEVELEASYBUILDMINCUSTOM=$CCC/easybuild/EasyBuild-custom-cscs-easybuild-devel
export EBROOTEASYBUILDMINCUSTOM=$CCC
export EBVERSIONEASYBUILDMINCUSTOM=cscs

export EASYBUILD_MODULES_TOOL=EnvironmentModulesC
if [ $ARCH = "gpu" ] ;then
    export EASYBUILD_OPTARCH=haswell
else
    export EASYBUILD_OPTARCH=broadwell
fi
export EASYBUILD_RECURSIVE_MODULE_UNLOAD=0
export LC_ALL=C

TTT=/dev/shm/piccinal
export EASYBUILD_BUILDPATH=$TTT/easybuild.jg/build/$ARCH
export EASYBUILD_TMPDIR=$TTT/easybuild.jg/$ARCH/tmp
# export XDG_RUNTIME_DIR=$SCRATCH/easybuild.jg/run/$ARCH

III=/apps/dom/UES/jenkins/7.0.UP00/$ARCH/easybuild/experimental
export EASYBUILD_PREFIX=$III
export EASYBUILD_INSTALLPATH=$III
module use $III/modules/all
echo $III/modules/all
module use /apps/dom/UES/sandbox/piccinal/7.0.UP00/$ARCH/easybuild/modules/all

echo 'export EASYBUILD_PREFIX=/apps/dom/UES/sandbox/piccinal/7.0.UP00/mc/easybuild'
echo 'export EASYBUILD_INSTALLPATH=$EASYBUILD_PREFIX'
echo 'export EASYBUILD_BUILDPATH=/tmp/eb.jg/tmp'
echo 'export EASYBUILD_TMPDIR=/tmp/eb.jg/build/mc'

