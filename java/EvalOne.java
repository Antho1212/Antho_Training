public class EvalOne {


    public static void main(String[] args) {
        int compteur = 1;

        System.out.println(compteur + " tentative(s) a(ont) été nécessaire(s) pour traverser !");
    }


    public static void deminer()  {

    }


    public static void creuser(){
        int value = (int) (Math.random() * 10);
        //génère un nombre aléatoire entre 1 et 10

    }


    public static boolean traverser() {
        return true;
    }
}

/**
 * Selon la norme java, les exceptions non-vérifiées et les exceptions vérifiées peuvent
 * recevoir un traitement différent en termes de spécification et de gestion (de l'exception).
 * En supposant qu'un de vos collègues ait suivi la norme java pour la spécification et
 * la gestion de l'exception (non-vérifiée), quelles différences trouverait-on
 * dans son code et ses spécifications, comparé aux vôtres (qui respectent
 * les bonnes pratiques vues dans le cours sur ce point)?
 *
 * - 1ère différence :
 * - 2ème différence :
 *
 * (Pensez différence entre exceptions vérifiées et non vérifiées d'un point
 * de vue documentation/spécification et pour le compilateur)
 */