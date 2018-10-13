program mpihel
implicit none

include 'mpif.h'

integer :: rank, size, ierr

call MPI_INIT(ierr)
call MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierr)
call MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierr)
write (*,*) 'Hello world! I am', rank, ' of ', size
call MPI_FINALIZE(ierr)      
end
