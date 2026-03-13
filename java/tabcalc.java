public class tabcalc{
    public static void main(String[] args){
        int tab [] = {1,2,3,4,5};
        tabcalc(tab,tab);
    }
    public static void tabcalc(int tab1[], tab2[]){
        /*
        @requires tab1 && tab2 > != 0;
        @return tab3 where tab3[i] = tab1[i] * sum of all elements in tab2;
        @throw exeption if tab1 or tab2 is empty;
        */
        if(tab1.length == 0 || tab2.length == 0) {
            throw new IllegalArgumentException("tab1 and tab2 must have at least one element");
        }
        int sum = 0;
        for (int i = 0; i < tab2.length; i++){
            sum += tab2[i];
        }
        int tab3 [] = new int [tab1.length];
        for (int i = 0; i < tab1.length; i++){
            tab3[i] = tab1[i] * sum;
        }           
    }
}