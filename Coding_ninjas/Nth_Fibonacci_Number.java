package Coding_ninjas;
// link - https://www.naukri.com/code360/problems/nth-fibonacci-number_74156?

import java.util.Scanner;

public class Nth_Fibonacci_Number {
    public static void main(String[] args) {

        /*
         * Your class should be named Solution.
         * Read input as specified in the question.
         * Print output as specified in the question.
         */

        Scanner scanner = new Scanner(System.in);
        int limit = scanner.nextInt();

        if (limit == 1 || limit == 2) {
            System.out.println(1);
            return;
        }
        limit -= 2;

        int a = 1, b = 1;
        while (limit > 0) {
            int temp = b;
            b = a + b;
            a = temp;
            limit--;
        }

        System.out.println(b);
        scanner.close();
    }
}
