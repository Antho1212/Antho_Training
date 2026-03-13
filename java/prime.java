public class prime{
    public static boolean isPrime(int p){
        /*
        @requires p > 0 ;
        @return true if p is prime, false otherwise;
        @throw exeption if p is less than or equal to 1;
        */
       if (p > 0){
            throw new IllegalArgumentException("p must be greater than 0");
       }
        for(int i = 1; i <= p; i++ ){
            if (p % i == 0){
                return false;
            }
        }
        system.out.println("true")
    }
}