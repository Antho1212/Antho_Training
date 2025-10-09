#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) { // give the result of the addition of number input
    if(argc = 3){
        printf("before swap : %d %d\n", argv[1], argv[2]);
        argv[1] = t;
        argv[1] = argv[2];
        argv[2] = t;
        printf("after swap : %d %d\n", argv[1], argv[2]);
        return EXIT_SUCCESS;
    }
    else{
        printf("please enter just two number");
        return EXIT_FAILURE;
    }
}