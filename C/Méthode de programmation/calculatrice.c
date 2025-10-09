#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main() {
    char input[100];
    double a, b, result;
    char op;

    while (1) {
        printf("Entrez une expression (ex: 2 + 3) ou 'q' pour quitter: ");
        fgets(input, sizeof(input), stdin);

        if (input[0] == 'q') {
            break;
        }

        if (sscanf(input, "%lf %c %lf", &a, &op, &b) != 3) {
            printf("Format invalide. Utilisez le format: <nombre> <opérateur> <nombre>\n");
            continue;
        }

        switch (op) {
            case '+':
                result = a + b;
                break;
            case '-':
                result = a - b;
                break;
            case '*':
                result = a * b;
                break;
            case '/':
                if (b == 0) {
                    printf("Erreur: Division par zéro.\n");
                    continue;
                }
                result = a / b;
                break;
            case '%':
                result = (int)a % (int)b;
                break;
            default:
                printf("Opérateur invalide. Utilisez +, -, *, /, ou %%.\n");
                continue;
        }
        printf("Le résultat est : %.2f\n", result);
    }
    return EXIT_SUCCESS;
}