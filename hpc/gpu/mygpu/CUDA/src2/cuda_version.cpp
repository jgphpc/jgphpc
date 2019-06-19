/*
 * grep "unsupported GNU" /opt/nvidia/cudatoolkit*/*/include/*/host_*.h |grep -v default

    -----------------   gcc/4   gcc/5   gcc/6   gcc/7   gcc/8   gcc/9
	cuda/08.0 < gcc/6   Y       Y       -       -       -       -

	cuda/09.0 < gcc/7   Y       Y       Y       -       -       -
	cuda/09.1 < gcc/7   Y       Y       Y       -       -       -

	cuda/09.2 < gcc/8   Y       Y       Y       Y       -       -
	cuda/10.0 < gcc/8   Y       Y       Y       Y       -       -

	cuda/10.1 < gcc/9   Y       Y       Y       Y       Y       -
    -----------------
	gcc4.9.3/gnu_version.exe__GNUC__=4
	gcc5.3.0/gnu_version.exe__GNUC__=5
	gcc6.2.0/gnu_version.exe__GNUC__=6
	gcc7.3.0/gnu_version.exe__GNUC__=7
	GCCcore8.3.0/gnu_version.exe__GNUC__=8
	GCCcore9.1.0/gnu_version.exe__GNUC__=9
    -----------------

* /opt/nvidia/cudatoolkit10/10.0.130_3.22-7.0.0.0_5.1__gdfb4ce5/include/crt/host_config.h
* https://stackoverflow.com/questions/6622454/cuda-incompatible-with-my-gcc-version
* https://github.com/enlighter/gpuocelot-git/blob/master/ocelot/ocelot/cuda/test/driver/generic.cpp
* cudatoolkit/10.0.130:
gcc/8.3.0: 10010
gcc/7.3.0: 10010

cuDriverGetVersion: 10010
Device 0: "Tesla P100-PCIE-16GB"
  CUDA Driver Version / Runtime Version     10.1 / 10.0
  CUDA Capability Major/Minor version number:    6.0
*/

#include <iostream>
#include <stdio.h>
#include <cuda_runtime.h>
#include <cuda.h>
#define report(x) std::cout << x << std::endl
 
int main(int argc, char *argv[])
{

	CUresult result = cuInit(0);
	if (result != CUDA_SUCCESS) {
		report("cuInit() failed: " << result);
		return 1;
	}

	int driverVersion = 0;
	result = cuDriverGetVersion(&driverVersion);
	if (result != CUDA_SUCCESS) {
		report("cuDriverGetVersion() failed: " << result);
	}
    std::cout << "cuDriverGetVersion: " << driverVersion << std::endl;
	
	int count = 0;
	result = cuDeviceGetCount(&count);
	if (result != CUDA_SUCCESS) {
		report("cuDeviceGetCount() failed: " << result);
		return 1;
	}

/*
	CUdevice device;
	result = cuDeviceGet(&device, 0);
	if (result != CUDA_SUCCESS) {
		report("cuDeviceGet() failed: " << result);
		return 1;
	}

	char devName[256] = {0};
	result = cuDeviceGetName(devName, 255, device);
	if (result != CUDA_SUCCESS) {
		report("cuDeviceGetName() failed: " << result);
		return 1;
	}
*/	

  printf("__GNUC__=%d\n", __GNUC__);
  int dev=0;
  int runtimeVersion = 0;
  struct cudaDeviceProp deviceProp;
  cudaGetDeviceProperties(&deviceProp, 0);
  // cudaGetDeviceProperties(&deviceProp, dev);
  printf("Device %d: \"%s\"\n", dev, deviceProp.name);
  cudaDriverGetVersion(&driverVersion);
  cudaRuntimeGetVersion(&runtimeVersion);
  printf("  CUDA Driver Version / Runtime Version     %d.%d / %d.%d\n",
    driverVersion/1000, (driverVersion%100)/10, runtimeVersion/1000,
    (runtimeVersion%100)/10);

  printf("  CUDA Capability Major/Minor version number:    %d.%d\n",
    deviceProp.major, deviceProp.minor);

/*
  printf("  (%2d) Multiprocessors, (%3d) CUDA Cores/MP:     %d CUDA Cores\n",
  deviceProp.multiProcessorCount,
  _ConvertSMVer2Cores(deviceProp.major, deviceProp.minor),
  _ConvertSMVer2Cores(deviceProp.major, deviceProp.minor)
                            * deviceProp.multiProcessorCount);

  printf("  GPU Max Clock rate:                            %.0f MHz (%0.2f GHz)\n",
    deviceProp.clockRate * 1e-3f, deviceProp.clockRate * 1e-6f);
  printf("  Theoretical peak performance per GPU:          %.0f Gflop/s\n",
    deviceProp.clockRate *1e-6f
    *_ConvertSMVer2Cores(deviceProp.major, deviceProp.minor)
    *deviceProp.multiProcessorCount);

  printf("  Maximum number of threads per multiprocessor:  %d\n",
    deviceProp.maxThreadsPerMultiProcessor);

  printf("  Peak number of threads:                        %d threads\n",
    deviceProp.multiProcessorCount
    *deviceProp.maxThreadsPerMultiProcessor );

  printf("  Maximum number of threads per block:           %d\n",
    deviceProp.maxThreadsPerBlock);
*/



/*
 * https://docs.nvidia.com/cuda/cuda-driver-api/group__CUDA__DEVICE.html#group__CUDA__DEVICE_1g9c3e1414f0ad901d3278a4d6645fc266
	int major, minor;
	result = cuDeviceComputeCapability(&major, &minor, device);
	if (result != CUDA_SUCCESS) {
		report("cuDeviceComputeCapability() failed: " << result);
		return 1;
	}
*/
    std::cout << count << std::endl;
//    std::cout << devName << std::endl;
/*
    int* version;
    cuDriverGetVersion(version);
    printf("cuDriverGetVersion=%d\n", version);
*/

    // step3: /proc/driver/nvidia
    char gpu_str[256] = "";
    printf("\n=== /proc/driver/nvidia/version ===\n");
    static const char filename[] = "/proc/driver/nvidia/version";
    FILE *file = fopen ( filename, "r" );
    if ( file != NULL ) {
        fgets ( gpu_str, sizeof gpu_str, file ) ;
        fputs ( gpu_str, stdout );
    }
    fclose(file);

    return 0;

}
