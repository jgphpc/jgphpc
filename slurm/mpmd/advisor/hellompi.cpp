#include <iostream>
#include <mpi.h>

// CC -dynamic -g hellompi.cpp -o INTEL

int main(int argc, char *argv[]) {
  int rank, size;

  MPI::Init(argc, argv);

  rank = MPI::COMM_WORLD.Get_rank();
  size = MPI::COMM_WORLD.Get_size();
  std::cout << "Hello world! I am " << rank << " of " << size << std::endl;

  MPI::Finalize();

  return 0;
}
