#include <stdio.h>
#include <stdlib.h>

void delete ( char string [] , char target ){ //fonction qui supprime toutes les occurrences d’un certain caractère dans une chaîne de caractères.
    int i;
    for(i = 0; string[i] != '\0'; i++){
        if (string[i] == target){
            string[i] = ' ';
        }
    }
}

int main (int argc, char* argv[]){
    if (argc < 2){
        printf("no argument \n");
        return EXIT_FAILURE;}
    else{
        for (int j = 1; j < argc; j++){
            delete(argv[j],'a'); 
            printf("%s ", argv[j]);}
            printf("\n");
        return EXIT_SUCCESS;}
}