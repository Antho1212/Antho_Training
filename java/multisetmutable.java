public class multisetmutable {
    // Deux tableaux pour stocker les éléments et leur nombre d'occurrences
    private String[] elements = new String[100];  // Les éléments uniques
    private int[] counts = new int[100];          // Le nombre d'occurrences
    private int nbElements = 0;                    // Nombre d'éléments uniques
    
    // Ajoute un élément au multiset
    public void add(String element) {
        // On cherche d'abord si l'élément existe déjà
        int index = -1;
        for (int i = 0; i < nbElements; i++) {
            if (elements[i].equals(element)) {
                index = i;
                break;
            }
        }
        
        if (index != -1) {
            // L'élément existe, on augmente son compte
            counts[index] = counts[index] + 1;
        } else {
            // L'élément n'existe pas, on l'ajoute
            elements[nbElements] = element;
            counts[nbElements] = 1;
            nbElements = nbElements + 1;
        }
    }
    
    // Supprime une occurrence d'un élément
    public void remove(String element) {
        // On cherche l'élément
        for (int i = 0; i < nbElements; i++) {
            if (elements[i].equals(element)) {
                // On trouve l'élément
                if (counts[i] > 1) {
                    // Il y a plusieurs occurrences, on diminue le compte
                    counts[i] = counts[i] - 1;
                } else {
                    // C'était la dernière occurrence, on supprime l'élément
                    // On décale tous les éléments après
                    for (int j = i; j < nbElements - 1; j++) {
                        elements[j] = elements[j + 1];
                        counts[j] = counts[j + 1];
                    }
                    nbElements = nbElements - 1;
                }
                break;
            }
        }
    }
    
    // Retourne le nombre d'occurrences d'un élément
    public int count(String element) {
        for (int i = 0; i < nbElements; i++) {
            if (elements[i].equals(element)) {
                return counts[i];
            }
        }
        return 0;  // L'élément n'existe pas
    }
    
    // Retourne le nombre total d'éléments (en comptant les doublons)
    public int size() {
        int total = 0;
        for (int i = 0; i < nbElements; i++) {
            total = total + counts[i];
        }
        return total;
    }
    
    // Affiche le contenu du multiset
    public void afficher() {
        System.out.print("{");
        for (int i = 0; i < nbElements; i++) {
            System.out.print(elements[i] + ": " + counts[i]);
            if (i < nbElements - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("}");
    }
    
    public static void main(String[] args) {
        // On crée un nouveau multiset
        multisetmutable fruits = new multisetmutable();
        
        // On ajoute des fruits
        fruits.add("pomme");
        fruits.add("orange");
        fruits.add("pomme");
        fruits.add("banane");
        fruits.add("pomme");
        
        System.out.println("=== Multiset de fruits ===");
        fruits.afficher();
        System.out.println("Nombre de pommes: " + fruits.count("pomme"));
        System.out.println("Nombre d'oranges: " + fruits.count("orange"));
        System.out.println("Nombre total d'éléments: " + fruits.size());
        
        // On supprime une pomme
        System.out.println("\n=== Après suppression d'une pomme ===");
        fruits.remove("pomme");
        fruits.afficher();
        System.out.println("Nombre de pommes: " + fruits.count("pomme"));
        
        // On supprime complètement les bananes
        System.out.println("\n=== Après suppression d'une banane ===");
        fruits.remove("banane");
        fruits.afficher();
        System.out.println("Nombre de bananes: " + fruits.count("banane"));
    }
}
