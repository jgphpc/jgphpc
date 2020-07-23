#include <stdio.h>

int main()
{
    int i,j;
    for ( i=0;i<10;i++ ) {
        j=i+1;
        printf("%d %d\n",i,j);
    }
    printf("Hello World from thread %d out of %d from process %d out of %d\n", 0, 1, 0, 1);

    return 0;
}
