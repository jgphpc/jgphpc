import os
import sys
import reframe as rfm
import reframe.utility.sanity as sn


@rfm.parameterized_test(*[[pe, cuda]
                          for pe in [['PrgEnv-pgi', 'pgi/19.10.0']]
                          # for pe in [['PrgEnv-pgi', 'pgi/20.1.0']]
                          for cuda in [
                              'cudatoolkit/10.0.130_3.22-7.0.1.0_5.2__gdfb4ce5',
                              # 'cudatoolkit/10.1.105_3.27-7.0.1.1_4.1__ga311ce7',
                              # 'cudatoolkit/10.2.89_3.28-7.0.1.1_2.1__g88d3d59',
                          ]
                          ])
class SphExaNativeCheck(rfm.RegressionTest):
    def __init__(self, pe, cuda):
        # {{{ pe
        self.descr = 'CI/CD test'
        self.valid_prog_environs = ['PrgEnv-gnu', 'PrgEnv-intel',
                                    'PrgEnv-cray', 'PrgEnv-cray_classic',
                                    'PrgEnv-pgi']
        # self.valid_systems = ['daint:gpu', 'dom:gpu']
        self.valid_systems = ['*']
        self.maintainers = ['JG']
        self.tags = {'sph'}
        # }}}

        # {{{ compile

# {{{ PGI: 
## > /opt/cray/pe/cdt/*/modulerc
## cdt/19.03 pgi/18.10.0
## cdt/19.08 pgi/19.5.0
## cdt/19.10 pgi/19.7.0  
## cdt/19.11 pgi/19.9.0  
## cdt/19.12 pgi/19.9.0  

## cdt/20.02 pgi/19.10.0 
## cdt/20.03 pgi/19.10.0 

## cdt/20.05 pgi/20.1.0  

## cdt/20.06 pgi/20.1.1  

## pgi/19.5.0
## pgi/19.7.0
## pgi/19.9.0
## pgi/19.10.0
## pgi/20.1.0  *

# CC -std=c++14 -O2 -mp -DNDEBUG -Isrc -Iinclude -DUSE_MPI  src/sqpatch/sqpatch.cpp -o bin/mpi+omp.app
# CC -std=c++14 -O2 -w -DNDEBUG -mp  -Isrc -Iinclude -DUSE_MPI -DUSE_OMP_TARGET src/sqpatch/sqpatch.cpp -o bin/mpi+omp+target.app
# acc: cdt/20.05 craype-accel-nvidia60 (cuda/10.1|10.0 -> 10.0 is not available)
# CC -std=c++14 -O2 -w  -mp -acc -ta=tesla,cc60 -Isrc -Iinclude -DNDEBUG -DUSE_MPI -DUSE_ACC -DUSE_STD_MATH_IN_KERNELS src/sqpatch/sqpatch.cpp -o bin/mpi+omp+acc.app
#
# cuda: non
# --expt-relaxed-constexpr
#  Experimental flag: Allow host code to invoke __device__ constexpr functions,
#  and device code to invoke __host__ constexpr functions.Note that the behavior
#  of this flag may change in future compiler releases.
# }}}
        self.testname = 'openacc'
        self.sourcesdir = 'src'
        prgenv = pe[0]
        compiler_version = pe[1]
        cuda_version = cuda.split('/')[1][0:4]
        # self.modules = [compilerversion, 'craype-accel-nvidia60', cuda]
        cdt = {
            'pgi/19.10.0': 'cdt/20.03',
            'pgi/20.1.0': 'cdt/20.05',
        }
        # self.modules = [compiler_version, cuda]
        self.modules = [cdt[compiler_version], 'craype-accel-nvidia60', cuda]
        self.prgenv_flags = {
            'PrgEnv-gnu': ['-I.', '-I./include', '-std=c++14', '-g', '-O3',
                           '-DUSE_MPI', '-DNDEBUG'],
            'PrgEnv-intel': ['-I.', '-I./include', '-std=c++14', '-g', '-O3',
                             '-DUSE_MPI', '-DNDEBUG'],
            'PrgEnv-cray': ['-I.', '-I./include', '-std=c++17', '-g', '-Ofast',
                            '-DUSE_MPI', '-DNDEBUG'],
            'PrgEnv-cray_classic': ['-I.', '-I./include', '-hstd=c++14', '-g',
                                    '-O3', '-hnoomp', '-DUSE_MPI', '-DNDEBUG'],
            'PrgEnv-pgi': ['-std=c++14', '-g', '-acc -ta=tesla,cc60']
        }
        self.build_system = 'SingleSource'
        # self.build_system.cxx = 'CC'
        self.sourcepath = '%s.cpp' % self.testname
        self.executable = '%s.exe' % self.testname

        # }}}

        # {{{ run
        ompthread = 1
        self.name = '{}_cuda{}_{}'.format(self.testname, cuda_version, compiler_version.replace('/', ''))
        self.num_tasks = 1
        self.num_tasks_per_node = 1
        self.num_cpus_per_task = ompthread
        self.num_tasks_per_core = 1
        self.use_multithreading = False
        self.exclusive = True
        self.time_limit = '1m'
        self.variables = {
            'CRAYPE_LINK_TYPE': 'dynamic',
            'OMP_NUM_THREADS': str(self.num_cpus_per_task),
        }
        self.executable_opts = ['4600']
        self.rpt = 'file.rpt'
        self.rpt_ldd = 'ldd.rpt'
        self.postbuild_cmds = [
            'module list -t',
            'ldd %s &> %s' % (self.executable, self.rpt_ldd),
            'file %s &> %s' % (self.executable, self.rpt)
        ]
        self.postrun_cmds = self.postbuild_cmds
        if cuda_version == '10.0':
            self.variables['LD_LIBRARY_PATH'] = '$CRAY_CUDATOOLKIT_DIR/lib64:$LD_LIBRARY_PATH'
        # }}}

        # {{{ sanity
        # sanity
        self.sanity_patterns = sn.all([
            # check the job output:
            sn.assert_found('_OPENACC version:', self.stdout),
        ])
        # }}}

    # {{{ compile hooks
    @rfm.run_before('compile')
    def set_compiler_flags(self):
        self.build_system.cxxflags = self.prgenv_flags[self.current_environ.name]
    # }}}
