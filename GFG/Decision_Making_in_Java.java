// link - https://www.geeksforgeeks.org/problems/java-if-else-decision-making0924/0

package GFG;

public class Decision_Making_in_Java {
    public static String compareNM(int n, int m) {
        if (n == m) {
            return "equal";
        } else if (n > m) {
            return "greater";
        } else {
            return "lesser";
        }
    }
}
