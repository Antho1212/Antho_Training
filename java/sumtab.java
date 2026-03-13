public class sumtab{
    public static void main(String[] args){
        int tab [] = {1,2,3,4,5};
        sumtab(tab);
    }
    public static void sumtab(int tab[]){
        /*
        @ requires tab = array of integers && tab.lenght > 0;
        @return sum of all elements in tab;
        @throw exeption if tab is empty;
        */
       if(tab.length == 0) {
            throw new IllegalArgumentException("tab must have at least one element");
       }
       int sum = 0;
       for (int i = 0; i < tab.length; i++){
            sum += tab[i];
       }
       System.out.println(sum);
    }
}