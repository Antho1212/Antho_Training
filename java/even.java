public class even{
    public static void main(string[] args){
        even(4);
    }
    public static void even(int n){
        /*
        @requires n >0;
        @return true if n is even, false otherwise;
        */
        if (n % 2 == 0){
            System.out.println("true");
        } else {
            System.out.println("false");    
        }
    }
}