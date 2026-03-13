public class pgcd{
    public static void main(String[] args){
        pgcd(3, 23);
    }
    public static void pgcd(int a, int b){
        /*@ requires a = integer && b = integer;
          @ ensure result = pgcd(a, b);
        */
        int a = 3;
        int b = 23;
        while (b > 0){
            int i = a % b;
            a = b;
            b = i;
        }
        System.out.println(a);
    }
}

