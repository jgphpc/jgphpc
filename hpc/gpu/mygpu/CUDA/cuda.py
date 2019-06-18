import os
import reframe as rfm
import reframe.utility.sanity as sn


@rfm.parameterized_test(*[[pe, cuda]
  for pe in [
    ['dom', 'PrgEnv-gnu', 'gcc/6.1.0'],
    ['dom', 'PrgEnv-gnu', 'gcc/7.3.0'],
    ['dom', 'PrgEnv-gnu', 'gcc/8.3.0'],
    ['dom', 'PrgEnv-gnu', 'GCCcore/8.3.0'],
    ['dom', 'PrgEnv-gnu', 'GCCcore/9.1.0'],
#daint:     ['daint', 'PrgEnv-gnu', 'gcc/4.9.3'],
#daint:     ['daint', 'PrgEnv-gnu', 'gcc/5.3.0'],
#daint:     ['daint', 'PrgEnv-gnu', 'gcc/6.2.0'],
#daint:     ['daint', 'PrgEnv-gnu', 'gcc/7.3.0'],
#daint: # mo use /apps/dom/UES/sandbox/piccinal/6.0.UP07/gpu/easybuild/modules/all
#daint: # https://gcc.gnu.org/releases.html
#daint: # https://mirror.kumi.systems/gnu/gcc/gcc-8.3.0/
#daint: # https://gcc.gnu.org/gcc-8/
#daint: # https://mirror.kumi.systems/gnu/gcc/gcc-9.1.0/
#daint: # https://gcc.gnu.org/gcc-9/
#daint:     ['daint', 'PrgEnv-gnu', 'GCCcore/8.3.0'],
#daint:     ['daint', 'PrgEnv-gnu', 'GCCcore/9.1.0'],
    ]
  for cuda in [
#    'cudatoolkit/8.0.61_2.4.9-6.0.7.0_17.1__g899857c',
#    'cudatoolkit/9.0.103_3.15-6.0.7.0_14.1__ge802626',
#    'cudatoolkit/9.1.85_3.18-6.0.7.0_5.1__g2eb7c52',
#    'cudatoolkit/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8',
     'cudatoolkit/10.0.130_3.22-7.0.0.1_3.3__gdfb4ce5',
    ]
  ])
#     ['daint', 'PrgEnv-gnu', 'gcc/4.9.3'],
#     ['daint', 'PrgEnv-gnu', 'gcc/5.3.0'],
#     ['daint', 'PrgEnv-gnu', 'gcc/6.2.0'],
#     ['daint', 'PrgEnv-gnu', 'gcc/7.3.0'],
#     ['daint', 'PrgEnv-intel', 'intel/17.0.4.196'],
#     ['daint', 'PrgEnv-intel', 'intel/18.0.2.199'],
#     ['daint', 'PrgEnv-cray', 'cce/8.6.1'],
#     ['daint', 'PrgEnv-cray', 'cce/8.7.4'],
#     ['daint', 'PrgEnv-pgi', 'pgi/17.5.0'],
#     ['daint', 'PrgEnv-pgi', 'pgi/18.5.0'],
#     ['daint', 'PrgEnv-pgi', 'pgi/18.10.0'],
#)
class CudaVersion(rfm.CompileOnlyRegressionTest):
    """
    grep "unsupported GNU" /opt/nvidia/cudatoolkit*/*/include/*/host_*.h
    -----------------   gcc/4   gcc/5   gcc/6   gcc/7   gcc/8   gcc/9
    cuda/08.0 < gcc/6   Y       Y       -       -       -       -

    cuda/09.0 < gcc/7   Y       Y       Y       -       -       -
    cuda/09.1 < gcc/7   Y       Y       Y       -       -       -

    cuda/09.2 < gcc/8   Y       Y       Y       Y       -       -
    cuda/10.0 < gcc/8   Y       Y       Y       Y       -       -

    cuda/10.1 < gcc/9   Y       Y       Y       Y       Y       -
    -----------------
[       OK ] cuda_8.0_daint_gcc4.9.3 on daint:gpu using PrgEnv-gnu
[       OK ] cuda_8.0_daint_gcc5.3.0 on daint:gpu using PrgEnv-gnu

[       OK ] cuda_9.0_daint_gcc4.9.3 on daint:gpu using PrgEnv-gnu
[       OK ] cuda_9.0_daint_gcc5.3.0 on daint:gpu using PrgEnv-gnu
[       OK ] cuda_9.0_daint_gcc6.2.0 on daint:gpu using PrgEnv-gnu

[       OK ] cuda_9.1_daint_gcc4.9.3 on daint:gpu using PrgEnv-gnu
[       OK ] cuda_9.1_daint_gcc5.3.0 on daint:gpu using PrgEnv-gnu
[       OK ] cuda_9.1_daint_gcc6.2.0 on daint:gpu using PrgEnv-gnu

[       OK ] cuda_9.2_daint_gcc4.9.3 on daint:gpu using PrgEnv-gnu
[       OK ] cuda_9.2_daint_gcc5.3.0 on daint:gpu using PrgEnv-gnu
[       OK ] cuda_9.2_daint_gcc6.2.0 on daint:gpu using PrgEnv-gnu
[       OK ] cuda_9.2_daint_gcc7.3.0 on daint:gpu using PrgEnv-gnu
--- dom:
[       NA ] cuda_10.0_dom_gcc6.1.0 on dom:gpu using PrgEnv-gnu
[       OK ] cuda_10.0_dom_gcc7.3.0 on dom:gpu using PrgEnv-gnu
TODO: cuda_10.1
    -----------------
    reframe --system dom:gpu --exec-policy=async --keep-stage-files \
            --prefix=$SCRATCH/reframe/ -r -c ./0.py
    """
    def __init__(self, pe, cuda):
    # def __init__(self, sysname, prgenv, compilerversion):
        super().__init__()
        sysname = pe[0]
        prgenv = pe[1]
        compilerversion = pe[2]
        cudashortver = cuda.split('/')[1][0:4]
        self.name = 'cuda_' + cudashortver + "_" + sysname + "_" + \
                    compilerversion.replace('/', '')
        self.descr = 'compilation only check'
        self.valid_systems = ['%s:gpu' % sysname]
        self.valid_prog_environs = [prgenv]
        self.modules = [compilerversion, cuda]
        self.prgenv_flags = {
            'PrgEnv-gnu': ['-I./include', '-std=c++14', '-O2', '-g',
                           '-fopenmp', '-D_JENKINS'],
            'PrgEnv-intel': ['-I./include', '-std=c++14', '-O2', '-g',
                             '-qopenmp', '-D_JENKINS'],
            'PrgEnv-cray': ['-I./include', '-hstd=c++14', '-O2', '-g',
                            '-homp', '-D_JENKINS'],
            'PrgEnv-pgi': ['-I./include', '-std=c++14', '-O2', '-g',
                           '-mp', '-D_JENKINS'],
        }
        self.variables = {
            'CRAYPE_LINK_TYPE': 'dynamic'
        }
        self.sourcesdir = os.path.join('src', 'Cuda')
        self.build_system = 'Make'
#        self.build_system = 'SingleSource'
        self.num_iterations = 100
        self.build_system.options = [
            'NVCCFLAGS="-arch=sm_60"', # P100
            'DDTFLAGS="-D_CSCS_ITMAX=%s"' % self.num_iterations,
            'LIB=-lstdc++']
        self.executable = 'jacobi'
        # self.testname = 'gnu_version'
        # self.testname = 'cuda_version'
        # self.sourcepath = '%s.cpp' % self.testname
        # self.executable = '%s.exe' % self.testname
        # self.rpt = '%s.rpt' % self.testname
        self.rpt = '%s.rpt' % self.executable
        self.maintainers = ['JG']
        self.tags = {'scs'}
        self.postbuild_cmd = ['file %s &> %s' % (self.executable, self.rpt)]
        self.sanity_patterns = sn.assert_found(
            'ELF 64-bit LSB executable, x86-64', self.rpt)

    def setup(self, partition, environ, **job_opts):
        super().setup(partition, environ, **job_opts)
        environ_name = self.current_environ.name
        prgenv_flags = self.prgenv_flags[environ_name]
        self.build_system.cxxflags = prgenv_flags
        self.build_system.ldflags = prgenv_flags
