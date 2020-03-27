#include <iostream>       // std::cout, std::endl
#include <thread>         // std::this_thread::sleep_for
#include <chrono>         // std::chrono::seconds
#include <omp.h>
 
int main() 
{
  #pragma omp parallel // private(tid, nthreads)
    {
    std::this_thread::sleep_for (std::chrono::seconds(10));
    }

  return 0;
}
