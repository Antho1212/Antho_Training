/*
 * Vous avez trouvé une faille dans l'interface d'une banque qui pourrait permettre une fuite d'une information : le
 * fait qu'un certain compte, identifié par son IBAN, existe bien au sein de cette banque. Mais vous savez que tester
 * tous les IBANs existants serait la meilleure façon d'être détecté par le système de sécurité de la banque. Vous
 * choisissez donc une approche plus subtile : ne tester que les IBANs syntaxiquement corrects.
 * Le but de IBAN.java est de générer une chaîne de caractères ressemblant à un identifiant de compte IBAN, comme
 * "BE34 7135 3223 5424". Ces identifiants doivent respecter une série de contraintes (purement fictives) :
 *   - ils doivent commencer par BE (nationalité de la banque)
 *   - les deux premiers chiffres doivent former un multiple de 17 (code de sécurité)
 *   - chaque premier chiffre des blocs de 4 chiffres doit être impair
 *   - la somme de tous les chiffres ne peut pas excéder 100
 *
 * Bonus : ajoutez la contrainte "l'IBAN doit contenir autant de nombres pairs et impairs"
 */

import java.util.Random;

class IBAN {
    static void print(Object o) {
        System.out.println(o);
    }

    public static void main(String[] args) {
        // Lancement du timer
        long startMs = System.currentTimeMillis();
        long startNs = System.nanoTime();

        // Recuperation des resultats
        String solution = generateAndTest();

        // Fin du timer
        long endMs = System.currentTimeMillis();
        long endNs = System.nanoTime();

        // Affichage des resultats
        print("---");
        print("IBAN généré: "+solution);
        print("---");
        print("Temps de calcul (ms): "+ (endMs-startMs));
        print("Temps de calcul (ns): "+ (endNs-startNs));
        print("---");
    }

    static String generateAndTest() {
        while(true){
            String iban = generate();
            if (test(iban) == true) {
                return iban;
            }
        }
    }

   
    static String generate() {
        Random rand = new Random();
        StringBuilder sb = new StringBuilder("BE");

        int[] multiples = {17, 34, 51, 68, 85};
        sb.append(multiples[rand.nextInt(multiples.length)]);

        for (int i = 0; i < 3; i++) {
            sb.append(" ");
            
            
            int premierChiffre = rand.nextInt(5) * 2 + 1; 
            sb.append(premierChiffre);
            
            
            for (int j = 0; j < 3; j++) {
                sb.append(rand.nextInt(10));
            }
        }
        return sb.toString();
    }

    static boolean test(String iban) {
    int somme = 0;
    for (char c : iban.toCharArray()) {
        if (Character.isDigit(c)) {
            somme += Character.getNumericValue(c);
        }
    };
    if (somme > 100) return false;
    else return true;
    }
}