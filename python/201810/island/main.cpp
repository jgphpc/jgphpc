#include <stdio.h>
#include "pi.h"

/*
### with c++ calls only:
FFF='-D_NOFORTRAN'
g++ $FFF -c pi.cpp -o pi.cpp.o
g++ -fPIC -shared -o libpi_cpp.so pi.cpp

g++ $FFF -c main.cpp -o main.cpp.o
g++ -o c.exe main.cpp.o -Wl,-rpath,$PWD/ libpi_cpp.dylib
./c.exe
# pi computed by c = 3.142096
*/

int main()
{
    const int num_points=10000;
    printf("num points=%d\n", num_points);
    printf("pi computed by c = %f\n", approximate_pi_c(num_points));
#ifndef _NOFORTRAN
    printf("pi computed by fortran = %f\n", approximate_pi_fortran(num_points));
#endif

    return 0;
}
