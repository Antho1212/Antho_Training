#include <stdio.h>
#include <stdlib.h>

void replace ( char string [] , char target , char replacement ){  //fonction qui remplace toutes les occurrences d’un certain caractère dans une chaîne de caractères par un autre caractère.
    int i;
    for(i = 0; string[i] != '\0'; i++){
        if (string[i] == target){
            string[i] = replacement;
        }
    }
}

int main (int argc, char* argv[]){
    if (argc < 2){
        printf("no argument \n");
        return EXIT_FAILURE;}
    else{
        for (int j = 1; j < argc; j++){
            replace(argv[j],'a','b'); 
            printf("%s ", argv[j]);}
            printf("\n");
        return EXIT_SUCCESS;}
