// CC -std=c++14  ./compilers_jg.cpp && ./a.out

#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

int main(){

#ifdef _CRAYC
//#define CURRENT_PE_ENV "CRAY"
    cout << "compiler: CCE/" << _RELEASE << "." << _RELEASE_MINOR << endl;
#endif

    //cout << "compiler: GNU/" << <<  << endl;
    
#ifdef __GNUC__
//#define CURRENT_PE_ENV "GNU"
    cout << "compiler: GNU/" << __GNUC__ << "." << __GNUC_MINOR__ 
        << "." << __GNUC_PATCHLEVEL__ 
        << endl;
#endif

#ifdef __INTEL_COMPILER
//#define CURRENT_PE_ENV "INTEL"
    cout << "compiler: INTEL/" << __INTEL_COMPILER << endl;
#endif

#ifdef __PGI
//#define CURRENT_PE_ENV "PGI"
    cout << "compiler: PGI/" << __PGIC__
         << "." << __PGIC_MINOR__
         << "." << __PGIC_PATCHLEVEL__
         << endl;
#endif

    return 0;
}

