#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>  //for toupper

void capitalize ( char string []){   //fonction qui affiche en majuscules une chaîne de caractères passée en paramètre.
    int index = 0;
    while(string[index] != '\0'){  //parcour le string
        string[index] = toupper(string[index]);
        index++;
    }
} 

void capitalize_ASCII ( char string []){
    int index = 0;
    while(string[index] != '\0'){  //parcour le string
        if (string[index] >='a' && string[index] <='z'){
        string[index] = string[index] - 32;
        index++;
        }
    }
}



int main (int argc, char* argv[]){
    if (argc < 2){
        printf("no argument \n");
        return EXIT_FAILURE;
    }
    else{
        for (int j = 1; j < argc; j++) {
            capitalize_ASCII(argv[j]);
            printf("%s ", argv[j]);
        }
        printf("\n");
        return EXIT_SUCCESS;
    }
}