public class activitertrain {
    public static void main(String[] args) {
    }
    int[][] activities = {{12,14}, {10,11}, {15,13}, {16,17}, {18,19}};
    int maxactivities(int[][] activities){
        activities = new int[activities.length];
        for (int i = 0; i < activities.length; i++) {
            activities[i] = activities[i][1];
        }
    }
}