// --- CSCS (Swiss National Supercomputing Center) ---
// samples/1_Utilities/deviceQuery/deviceQuery.cpp

#include <stdio.h>
#include <helper_cuda.h>

extern "C"
void set_gpu(int dev)
{
  cudaSetDevice(dev);
}

extern "C"
void get_gpu_info(char *gpu_string, int dev)
{
  struct cudaDeviceProp dprop;
  cudaGetDeviceProperties(&dprop, dev);
  strcpy(gpu_string,dprop.name);
}

extern "C"
void get_more_gpu_info(int dev)
{
  int driverVersion = 0, runtimeVersion = 0;
  struct cudaDeviceProp deviceProp;
  cudaGetDeviceProperties(&deviceProp, dev);

  printf("Device %d: \"%s\"\n", dev, deviceProp.name);
  cudaDriverGetVersion(&driverVersion);
  cudaRuntimeGetVersion(&runtimeVersion);
  printf("  CUDA Driver Version / Runtime Version     %d.%d / %d.%d\n", 
    driverVersion/1000, (driverVersion%100)/10, runtimeVersion/1000, 
    (runtimeVersion%100)/10);

  printf("  CUDA Capability Major/Minor version number:    %d.%d\n", 
    deviceProp.major, deviceProp.minor);

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

//  printf("  Maximum number of threads per multiprocessor:  %d\n", 
//    deviceProp.maxThreadsPerMultiProcessor);

  printf("  Peak number of threads:                        %d threads\n", 
    deviceProp.multiProcessorCount 
    * deviceProp.maxThreadsPerMultiProcessor );

  printf("  Maximum number of threads per block:           %d\n", 
    deviceProp.maxThreadsPerBlock);

  // --- deviceQuery.cpp ---
  // https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__DEVICE.html
  printf("\nDevice %d: \"%s\"\n", dev, deviceProp.name);
  printf("  Warp size: %d\n", deviceProp.warpSize);    
  printf("  Maximum number of threads per multiprocessor:  %d\n",
          deviceProp.maxThreadsPerMultiProcessor);
  printf("  Maximum number of threads per block:           %d\n",
          deviceProp.maxThreadsPerBlock);
  printf("  Max dimension size of a thread block (x,y,z): (%d, %d, %d)\n",
          deviceProp.maxThreadsDim[0], deviceProp.maxThreadsDim[1],
          deviceProp.maxThreadsDim[2]);
  printf("  Max dimension size of a grid size    (x,y,z): (%d, %d, %d)\n",
          deviceProp.maxGridSize[0], deviceProp.maxGridSize[1],
          deviceProp.maxGridSize[2]);
  printf("  Device has ECC support:                        %s\n",
          deviceProp.ECCEnabled ? "Enabled" : "Disabled");
  printf("  multiProcessorCount:                           %d\n",
          deviceProp.multiProcessorCount);

  // summary table
  printf("%10s| %7s | %7s | %7s | %7s |\n", " ", "thread", "warp", "sm", "device");
  printf("threads   | %7d | %7d | %7d | %7d |\n", 
          1, deviceProp.warpSize, deviceProp.maxThreadsPerMultiProcessor, 
          deviceProp.multiProcessorCount * deviceProp.maxThreadsPerMultiProcessor);
  printf("warps     | %7s | %7d | %7d | %7d |\n", "x", 1,
          deviceProp.maxThreadsPerMultiProcessor / deviceProp.warpSize,
          (deviceProp.multiProcessorCount * deviceProp.maxThreadsPerMultiProcessor) / deviceProp.warpSize);
  printf("sms       | %7s | %7s | %7d | %7d |\n", "x", "x", 1, deviceProp.multiProcessorCount);
  printf("%-.10s| %7s | %7s | %7s | %7d |\n", deviceProp.name, "x", "x", "x", 1);

/*
          |  thread |    warp |      sm |  device |
threads   |       1 |      32 |    2048 |  114688 |
warps     |       x |       1 |      64 |    3584 |
sms       |       x |       x |       1 |      56 |
Tesla P100|       x |       x |       x |       1 |
*/

}

