#include <stdio.h>
#include <bitmask.h>
#include <cpuset.h>

// cc h.c -lcpuset
int main (int argc, char *argv[])
{
      // int v;
      // v=cpuset_version();

  printf("%s %d\n","cpuset_version=",cpuset_version());
  printf("%s %d\n","cpuset_size=",cpuset_size());
  printf("%s %d\n","cpuset_where=",cpuset_where());
  return 0;
}
