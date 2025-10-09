#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {  //calculate
    if(argc != 4) {
        printf("Usage: %s <num1> <operator> <num2>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[3]);
    int result;

    if(strcmp(argv[2], "+") == 0) {
        result = a + b;
    } else if(strcmp(argv[2], "-") == 0) {
        result = a - b;
    } else if(strcmp(argv[2], "*") == 0) {
        result = a * b;
    } else if(strcmp(argv[2], "/") == 0) {
        result = a / b;
    } else {
        printf("Invalid operator\n");
        return EXIT_FAILURE;
    }

    printf("the result is : %d\n", result);
    return EXIT_SUCCESS;
}