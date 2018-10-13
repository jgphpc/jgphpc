program main

!### with fortran calls only:
! FFF='-cpp -D_NOC -fno-leading-underscore' # -fno-underscoring
! gfortran $FFF -c pi.f90 -o pi.f90.o
! nm pi.f90.o |grep pi_f
! gfortran -shared -o libpi_fortran.dylib pi.f90.o
! ---
! FFF='-cpp -D_NOC'
! gfortran $FFF -c pi.f90 -o pi.f90.o
! gfortran -shared -o libpi_fortran.dylib pi.f90.o
! gfortran $FFF -c main.f90 -o main.f90.o
! gfortran -o f.exe main.f90.o -Wl,-rpath,$PWD/ libpi_fortran.dylib
! ./f.exe
! # pi computed by fortran =    3.1040000915527344

    use, intrinsic :: iso_c_binding, only: c_double, c_int
    use pi, only: approximate_pi_fortran

    implicit none

#ifndef _NOC
    interface approximate_pi_c
        function approximate_pi_c(num_points) bind (c)
            import :: c_double, c_int
            integer(c_int), value :: num_points
            real(c_double) :: approximate_pi_c
        end function
    end interface
#endif

    integer, parameter :: num_points=10000
    print *,"num points=", num_points 
    print *,"pi computed by fortran = ", approximate_pi_fortran(num_points)
#ifndef _NOC
    print *, "pi computed by c = ", approximate_pi_c(num_points)
#endif

end program
