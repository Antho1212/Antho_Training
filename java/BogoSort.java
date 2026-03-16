/*
 * Le but de BogoSort.java est d'implémenter l'algorithme de BogoSort. Cet algorithme naïf consiste à générer une
 * permutation aléatoire d'une liste donnée et de vérifier si cette permutation est triée. Tant qu'on ne trouve pas de
 * permutation triée, on en crée de nouvelles.
 *
 * Indice: si la génération d'une permutation aléatoire pose souci, consultez l'implémentation Java disponible à
 * https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
 *
 * Bonus: implémentez une version déterministe de BogoSort qui parcourt toutes les permutations dans un certain ordre
 * plutôt que de les générer au hasard.
 */

import java.util.Arrays;

class BogoSort {
    static void print(Object o) {
        System.out.println(o);
    }

    public static void main(String[] args) {
        // Lancement du timer
        long startMs = System.currentTimeMillis();
        long startNs = System.nanoTime();

        // Les variables propres au probleme
        int n = 9;
        int[] toSort = new int[n];
        for (int i = 0 ; i < n ; i++)
            toSort[i] = n-i;  // Descending order

        // Recuperation des resultats
        int[] sorted = generateAndTest(toSort);

        // Fin du timer
        long endMs = System.currentTimeMillis();
        long endNs = System.nanoTime();

        // Affichage des resultats
        print("---");
        print("Starting list: "+Arrays.toString(toSort));
        print("Sorted list: "+Arrays.toString(sorted));
        print("---");
        print("Temps de calcul (ms): "+ (endMs-startMs));
        print("Temps de calcul (ns): "+ (endNs-startNs));
        print("---");
    }

    static int[] generateAndTest(int[] toSort) {
        while(true){
            int[] permutate = generate(toSort);
            if (test(permutate) == true) {
                return permutate;
            }
        }
    }

    static int[] generate(int[] tosort) {
        java.util.Random rand = new java.util.Random();
        int[] copie = Arrays.copyOf(tosort, tosort.length);
        for (int i = tosort.length - 1; i > 0; i--) {
            int j = rand.nextInt(i + 1);
            
            int temp = copie[i];
            copie[i] = copie[j];
            copie[j] = temp;
        }
        return copie;
    }

    static boolean test(int[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] > array[i + 1]) {
                return false;
            }
        }
        return true;
    }
}