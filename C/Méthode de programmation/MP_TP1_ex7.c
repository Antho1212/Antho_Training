#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) { // programme qui multiplie deux entiers positifs a et b selon le principe suivant :a ∗ b = a ∗ (b − 1) + a Si b est impair a ∗ b = (2 ∗ a) ∗ (b/2) Si b est pair et différent de 0
    if(argc == 3){
        unsigned int a = atoi(argv[1]);
        unsigned int b = atoi(argv[2]);
        unsigned int result = 0;
        if(b % 2 == 0 && b !=0){
            result = (2*a)*(b/2);
            printf("the result is %d\n", result);
            return EXIT_SUCCESS;
        }
        else{
            result = a*(b-1);
            printf("the result is %d\n", result);
            return EXIT_SUCCESS;
        }
    }
    else{
        printf("please enter just two number\n");
        return EXIT_FAILURE;
    }
}