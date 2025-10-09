#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) { // divide two positif integer without / operation and give the quotient and rest
    if(argc == 3){
        int a = atoi(argv[1]);
        int b = atoi(argv[2]);
        int quotient = 0;
        int rest = 0;
        if(a<b){
            while(a<b){
                b = b - a;
                quotient ++;
            }
            rest = b;
            printf("the quotient is %d and the rest is %d\n", quotient, rest);
            return EXIT_SUCCESS;
        }
        else{
            while(a>b){
                a = a - b;
                quotient ++;
            }
            rest = a;
            printf("the quotient is %d and the rest is %d\n", quotient, rest);
            return EXIT_SUCCESS;
        }
    }
    else{
        printf("please enter just two number\n");
        return EXIT_FAILURE;
    }
}