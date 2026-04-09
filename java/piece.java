public class piece{
    public static void main(String[] args) {
        bestpiece(54);
    }

    public static void piecetry(int value) {
        int piece_20 = 0;
        int piece_10 = 0;
        int piece_5 = 0;
        int piece_2 = 0;
        int piece_1 = 0;
        while(value >0){
            if(value > 20){
                value -=20;
                piece_20++;
            }
            else if(value > 10){
                value -=10;
                piece_10++;
            }
            else if(value > 5){
                value -=5;
                piece_5++;
            }
            else if(value > 2){
                value -=2;
                piece_2++;
            }
            else{
                value -=1;
                piece_1++;
            }
        }
        System.out.println("Piece of 20: " + piece_20);
        System.out.println("Piece of 10: " + piece_10);
        System.out.println("Piece of 5: " + piece_5);
        System.out.println("Piece of 2: " + piece_2);
        System.out.println("Piece of 1: " + piece_1);
    }

    public static void bestpiece(int value){
        int[] devises = {20, 10, 5, 2, 1};
        int[] count = new int[devises.length];
        int maxIndex = 0;
        for (int i = 0; i < devises.length; i++) {
            count[i] = value / devises[i];
            value = value % devises[i];
            if (count[i] > count[maxIndex]) maxIndex = i;
        }
        for (int i = 0; i < devises.length; i++) {
            System.out.println("Piece of " + devises[i] + ": " + count[i]);
        }
        System.out.println("Best piece: " + devises[maxIndex]);
    }
}