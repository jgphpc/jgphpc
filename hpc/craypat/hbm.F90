program hbmtest 
! was Cray case 172060:
! perftools-lite-hbm fails to compile fortran code using ieee_arithmetic
! undefined reference to $data_init$ieee_exceptions__offset4096__cray_memtr_lineno 
    use ieee_arithmetic 
    use mpi 
    implicit none 
    integer :: ierr 
    double precision :: x 
    call MPI_INIT(ierr) 
    x=0.0 
    if ( ieee_is_nan(x) ) then 
        print *,0 
    endif 
    call MPI_FINALIZE(ierr) 
end program hbmtest 
