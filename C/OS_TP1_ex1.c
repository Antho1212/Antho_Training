#include <stdio.h>
#include <stdlib.h>
#include <string.h>  //for strlen

//version avec strlen()
unsigned int string_length ( char string []){ //renvoie le nombre de caractère dans une chaine de caracteres
    unsigned int length = strlen(string);
    return length;
}

//version sans strlen()

size_t string_length_2 ( const char string[]){ //renvoie le nombre de caractère dans une chaine de caracteres
    size_t length_2 = 0;
    while (string[length_2] != '\0'){
        length_2 ++;
    }   
    return length_2;
}

int main(void){
    printf("the result is %u \n",string_length("Bonjour"));
    printf("the second result is %zu \n ", string_length_2("Salut"));
    return EXIT_SUCCESS;
}
