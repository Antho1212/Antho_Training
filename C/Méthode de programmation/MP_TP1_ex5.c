#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) { // give divider of a number in input
    if(argc == 2){
        int a = atoi(argv[1]);
        if(a<1){
            printf("enter a number higher than 1\n");
        }
        int i = a;
        while(i > 0){
            if(a % i == 0){
                printf("%d : is a divide of %d\n", i, a);
                i--;
            }
            i--;
        }
        return EXIT_SUCCESS;
    }
    else{
        printf("please enter just one number\n");
        return EXIT_FAILURE;
    }
}