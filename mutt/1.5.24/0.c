#include <stdio.h>
#include <string.h>

int main() {

        char s1[1024]="[cscs.ch #12153] How to set";
        //char s2[4]="";
        //char* sloc="";
        char* s2="";
        char s3[5]="";
        int nombre=5;
        char delim='#';
 
        printf ("s1 \"%s\" s2 \"%s\"\n", s1,s2);
        s2 = strchr( s1, delim ); s2++;
        printf ("s1 \"%s\" s2 \"%s\"\n", s1,s2);
        strncpy(s3, s2, nombre);
        s3[nombre]='\0';
        printf ("s1 \"%s\" s2 \"%s\" s3 \"%s\"\n", s1,s2,s3);

        return 0;

}
