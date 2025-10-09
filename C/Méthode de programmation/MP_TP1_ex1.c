#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) { // give the result of the addition of number input
    if(argc < 3){
        printf("please enter at least two number");
        return EXIT_FAILURE;
    }
    else{
        double result = 0;
        for(int i=1; i <argc; i++){
            result += atof(argv[i]);
        }
        printf("the result is : %.3lf\n", result); //give the result with 3 after the coma
        return EXIT_SUCCESS;
    }
}