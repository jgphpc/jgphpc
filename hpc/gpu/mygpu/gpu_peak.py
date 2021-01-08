import os

import reframe as rfm
import reframe.utility.sanity as sn


@rfm.simple_test
class GpuTest(rfm.RegressionTest):
    """
    PERFORMANCE REPORT
    GpuTest
    - dom:gpu
       - PrgEnv-gnu
          * num_tasks: 1
          * driver: 450.51
          * cuda_driver_version: 11.0
          * cuda_runtime_version: 11.0
          * cuda_capability: 6.0 (Tesla P100-PCIE-16GB)
          * peak_perf: 4761 Gflop/s

~/reframe.git/bin/reframe -C ~/reframe.git/config/cscs.py --system ault:intelv100 \
--keep-stage-files -v -c gpu_peak.py -r --performance-report  # sacct is slow -> patience...
    GpuTest
    - ault:intelv100
       - PrgEnv-gnu
          * num_tasks: 1
          * driver: 455.32
          * cuda_driver_version: 11.1
          * cuda_runtime_version: 11.1
          * cuda_capability: 7.0 (Tesla V100-PCIE-16GB)
          * peak_perf: 7066 Gflop/s
    """
    def __init__(self):
        self.descr = 'GPU specs test'
        self.maintainers = ['JG']
        self.valid_systems = ['daint:gpu', 'dom:gpu',
                              'arolla:cn', 'tsa:cn',
                              'ault:amdv100', 'ault:intelv100',
                              'ault:amda100', 'ault:amdvega']
        self.valid_prog_environs = ['PrgEnv-gnu']
        self.sourcesdir = 'src'
        self.build_system = 'Make'
        self.executable = './exe'

        # {{{ run
        self.num_tasks = 1
        self.num_tasks_per_node = 1
        self.num_cpus_per_task = 1
        self.num_tasks_per_core = 1
        # self.use_multithreading = False
        # self.exclusive = True
        # self.exclusive_access = True
        self.time_limit = '1m'
        self.prerun_cmds = ['module list']
        # }}}

        # {{{ sanity_patterns
        self.sanity_patterns = sn.all(
            [
                sn.assert_not_found(r'MapSMtoCores.*is undefined', self.stdout),
                sn.assert_found(r'Kernel Module', self.stdout),
                sn.assert_found(r'CUDA Driver Version / Runtime', self.stdout),
                sn.assert_found(r'CUDA Capability Major/Minor', self.stdout),
                sn.assert_found(r'Theoretical peak performance', self.stdout),
                sn.assert_found(r'^Device ', self.stdout),
                # sn.assert_found(r'', self.stdout),
            ]
        )
        # self.sanity_patterns = self.assert_num_tasks()
        # }}}

        # {{{ performance
        regex1 = r'Kernel Module\s+(\S+)\.\d+\s+'
        regex2 = r'\s+CUDA Driver Version / Runtime Version\s+(\S+) / (\S+)'
        regex3 = r'\s+CUDA Capability Major/Minor version number:\s+(\S+)'
        regex4 = r'Theoretical peak performance per GPU:\s+(\S+) Gflop/s'
        self.perf_patterns = {
            'driver': sn.extractsingle(regex1, self.stdout, 1, float),
            'cuda_driver_version': sn.extractsingle(regex2, self.stdout, 1,
                                                    float),
            'cuda_runtime_version': sn.extractsingle(regex2, self.stdout, 2,
                                                     float),
            'cuda_capability': sn.extractsingle(regex3, self.stdout, 1, float),
            'peak_perf': sn.extractsingle(regex4, self.stdout, 1, int),
        }
        self.reference = {
            'dom:gpu': {
                'peak_perf': (4761, -0.10, None, 'Gflop/s'),
            },
            'daint:gpu': {
                'peak_perf': (4761, -0.10, None, 'Gflop/s'),
            },
            'ault:intelv100': {
                'peak_perf': (5500, -0.10, None, 'Gflop/s'),
            },
            'ault:amda100': {
                'peak_perf': (15000, -0.10, None, 'Gflop/s'),
            },
            'ault:amdv100': {
                'peak_perf': (5500, -0.10, None, 'Gflop/s'),
            },
            'ault:amdvega': {
                'peak_perf': (3450, -0.10, None, 'Gflop/s'),
            },
            'arolla:cn': {
                'peak_perf': (5861, -0.10, None, 'Gflop/s'),
            },
            'tsa:cn': {
                'peak_perf': (5861, -0.10, None, 'Gflop/s'),
            },
            '*': {'driver': (0, None, None, ''),
                  'cuda_driver_version': (0, None, None, ''),
                  'cuda_runtime_version': (0, None, None, ''),
                  'cuda_capability': (0, None, None, '')},
        }
        # }}}

    # {{{ hooks
    # {{{ set_gpu_arch
    @rfm.run_before('compile')
    def set_gpu_arch(self):
        cs = self.current_system.name
        cp = self.current_partition.fullname
        gpu_arch = None
        if cs in {'dom', 'daint'}:
            gpu_arch = '60'
            self.modules = ['cdt-cuda/20.11', 'craype-accel-nvidia60']
            self.build_system.cppflags = [
                '-I$CUDATOOLKIT_HOME/samples/common/inc'
            ]
        elif cs in {'ault'}:
            # self.modules = ['cuda']
            if cp in {'ault:amdv100', 'ault:intelv100'}:
                self.prebuild_cmds += [
                    # 'module use /users/piccinal/git/spack.git/share/spack/modules/linux-centos7-skylake_avx512',
                    # 'module load cuda-11.2.0-gcc-8.3.0-xhe7m3f',
                    'module load gcc/10.1.0',
                ]
                # cuda_path = '/users/piccinal/git/spack.git/opt/spack/linux-centos7-skylake_avx512/gcc-8.3.0/cuda-11.2.0-xhe7m3frbxqrtmby3nccewsz2ch2g3gy'
                cuda_path = '/users/piccinal/.local/easybuild/software/nvhpc/2020_2011-cuda-11.1/Linux_x86_64/20.11/compilers'
                self.variables = {
                    'CUDATOOLKIT_HOME': f'{cuda_path}',
                    'PATH': f'{cuda_path}/bin:$PATH',
                    # examples/OpenACC/SDK/include/helper_string.h
                }
                # self.modules = ['cuda-11.2.0-gcc-8.3.0-xhe7m3f', 'gcc/10.1.0']
                self.build_system.cc = 'gcc'
                self.build_system.cppflags = [
                    '-I/users/piccinal/.local/easybuild/software/cuda-samples/11.2/Common',
                ]
                self.build_system.ldflags = [
                    '-Wl,-rpath,$CUDATOOLKIT_HOME/../cuda/11.1/targets/x86_64-linux/lib ',
                    '-Wl,-rpath,$CUDATOOLKIT_HOME/lib ',
                    '-L$CUDATOOLKIT_HOME/../cuda/11.1/targets/x86_64-linux/lib',
                    # '-L$CUDATOOLKIT_HOME/lib',
                    '-lcudart', # '-lcudanvhpc',
                ]
                gpu_arch = '70'
            elif cp in {'ault:amda100'}:
                gpu_arch = '80'
        elif cs in {'arola', 'tsa'}:
            gpu_arch = '70'
            self.modules = ['cuda/10.1.243']

        if gpu_arch:
            self.build_system.makefile = 'makefile.cuda'
            self.build_system.cflags = ['-g']
            self.build_system.cxxflags = [f'-arch=compute_{gpu_arch}',
                                          f'-code=sm_{gpu_arch}']
            return

        # AMD options
        if cp in {'ault:amdvega'}:
            self.modules = ['rocm']
            gpu_arch = 'gfx906'

        if gpu_arch:
            self.build_system.cxxflags = [f'--amdgpu-target={gpu_arch}']
            self.build_system.makefile = 'makefile.hip'
    # }}}

    # {{{ get device
    @rfm.run_before('performance')
    def get_device(self):
        regex5 = r'^Device \d+: \"(.*)\"$'
        rptf = os.path.join(self.stagedir, sn.evaluate(self.stdout))
        device = sn.extractsingle(regex5, rptf, 1)
        for key in self.reference.keys():
            if key.endswith(':cuda_capability'):
                self.reference[key] = (0, None, None, f'({device})')
    # }}}

#     # {{{ this works too, keep as reminder:
#     @rfm.run_before('performance')
#     def update_reference(self):
#         ref = {}
#         for key in self.reference.keys():
#             ref[key] = self.reference[key]
#
#         for key in self.reference.keys():
#             for vv in ['driver', 'cuda_driver_version',
#                        'cuda_runtime_version', 'cuda_capability']:
#                 upkey = f'{key.split(":")[0]}:{key.split(":")[1]}:{vv}'
#                 ref[upkey] = (0, None, None, '')
#
#         for key in ref.keys():
#             self.reference[key] = ref[key]

        # print('ref=', self.reference)
        # }}}
    # }}}
