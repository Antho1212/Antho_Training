public class EvalOne {


    public static void main(String[] args) {
        int compteur = 1;
        while(!traverser()){
            compteur++;
        }
        System.out.println(compteur + " tentative(s) a(ont) été nécessaire(s) pour traverser !");
    }

    /**
     * Démine un terrain de mines
     * pertmet de détecter les mines explosives et incendiaires si elles sont trouvées.
     * @throws UndetectedMineException si une mine non détectée explose
     */
    public static void deminer() throws UndetectedMineException{
        try {
        creuser();
        System.out.println("aucune mine détectée");
    } 
    catch (ExplosiveMineException e) {
        System.out.println("Mine explosive détectée");
    } 
    catch (IncendiaryMineException e) {
        System.out.println("Mine incendiaire détectée");
    }
    }


    /**
     *  @throws ExplosiveMineException si une mine explosive est découverte
     *  @throws IncendiaryMineException si une mine incendiare est découverte
     *  @throws UndetectedMineException si une mine n'a pas été détecter
     */
    public static void creuser() throws ExplosiveMineException, IncendiaryMineException, UndetectedMineException{
        int value = (int) (Math.random() * 10);
        //génère un nombre aléatoire entre 1 et 10
        if(value <= 2){
            throw new ExplosiveMineException("mine explisve détecter");
        }
        else if(value <= 4){
            throw new IncendiaryMineException("mine incendiaire détecter");
        }
        else if(value <= 6){
            throw new UndetectedMineException("mine non détecter");
        }
    }

    /**
     * Tente de traverser le champ de mines.
     * @return true si les 10 pas sont franchis, false si une mine undétecter explose.
     */
    public static boolean traverser() {
        try {
            for (int i = 0; i < 10; i++) {
            deminer();
            }
            return true;
        } catch (UndetectedMineException e) {
            System.out.println("Boum !");
            return false;
        }
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
 * - 1ère différence : les exeptions non vérifiées ne doivent pas obligatoirement etre spécifier alors que dans le cours si
 * - 2ème différence : les exeptions non vérifiées ne doivent pas obligatoirement etre dans la signature alors que dans le cours si
 *
 * (Pensez différence entre exceptions vérifiées et non vérifiées d'un point
 * de vue documentation/spécification et pour le compilateur)
 */