/*
 * Vous disposez d'un échiquier de taille 4x4. Le but de EightQueens.java est de placer 4 reines sur cet échiquier
 * sans qu'aucune ne menace directement une autre reine.
 *
 * Bonus: généralisez le problème pour pouvoir placer n dames sur un échiquier de n x n.
 */

class EightQueens {
    static void print(Object o) {
        System.out.println(o);
    }

    public static void printBoard(int[][] board) {
        for (int[] row : board) {
            for (int cell : row) {
                if (cell == 1) {
                    System.out.print(" Q ");
                } else {
                    System.out.print(" . ");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        // Lancement du timer
        long startMs = System.currentTimeMillis();
        long startNs = System.nanoTime();

        // Les variables propres au probleme
        int n = 8;
        int[][] emptyBoard = new int[n][n];  // 0 = empty, 1 = queen

        // Recuperation des resultats
        int[][] boardWithQueens = generateAndTest(emptyBoard);

        // Fin du timer
        long endMs = System.currentTimeMillis();
        long endNs = System.nanoTime();

        // Affichage des resultats
        print("---");
        print("Solution: ");
        printBoard(boardWithQueens);
        print("---");
        print("Temps de calcul (ms): "+ (endMs-startMs));
        print("Temps de calcul (ns): "+ (endNs-startNs));
        print("---");
    }

    static int[][] generateAndTest(int[][] boardToFill){
        while(true){
            generate(boardToFill);
            if (test(boardToFill) == true) {
                return boardToFill;
            }
        }
    }

   
    static void generate(int[][] board) {
        int n = board.length;
        int [] columns = new int[n];
        java.util.Random rand = new java.util.Random();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = 0; // Clear the board
            }
        }
        for (int i = 0; i < n; i++) columns[i] = i;
        
        for (int i = n - 1; i > 0; i--) {
        int j = rand.nextInt(i + 1);
        int temp = columns[i];
        columns[i] = columns[j];
        columns[j] = temp;
        }
        for (int i = 0; i < n; i++) {
            board[i][columns[i]] = 1; // Place a queen
        }
    }

    static boolean test(int[][] board){
        //test if the queens are not on the same diagonal
        int n = board.length;
        int[] pos = new int[n];

       
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    pos[i] = j;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (Math.abs(i - j) == Math.abs(pos[i] - pos[j])) {
                    return false;
                }
            }
        }
        return true;
    }
}