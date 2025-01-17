// https://www.geeksforgeeks.org/problems/while-loop-printtable-java/1

package GFG.Basics;

import java.util.Scanner;

public class While_Loop_Print_Table_Java {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int max = n * 10;
        while (max > 0) {
            System.out.print(max + " ");
            max -= n;
        }
        scanner.close();
        return;
    }
}
