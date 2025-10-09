#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) { // say if a number in input is odd or even
    if(argc == 2){
        int a = atoi(argv[1]);
        if(a %2 == 0){
            printf("%d : is even\n",a);
            return EXIT_SUCCESS;
        }
        else{
            printf("%d : is odd\n",a);
            return EXIT_SUCCESS;
        }
    }
    else{
        printf("please enter just one number\n");
        return EXIT_FAILURE;
    }
}