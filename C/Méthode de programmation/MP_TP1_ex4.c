#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) { // give the biggest int of a list
    if(argc < 2){
        printf("please enter at least one number\n");
        return EXIT_FAILURE;
    }
    else{
        int a = atoi(argv[1]);
        for(int i=2;i < argc; i++){
            if(a < atoi(argv[i])){
                a = atoi(argv[i]);
            }
        }
        printf("the biggest is : %d\n", a);
        return EXIT_SUCCESS;
    }
}