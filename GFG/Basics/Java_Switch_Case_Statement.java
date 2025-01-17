// link - https://www.geeksforgeeks.org/problems/java-switch-case-statement3529/1

package GFG.Basics;

import java.util.List;

public class Java_Switch_Case_Statement {
    static double switchCase(int choice, List<Double> arr) {
        switch (choice) {
            case 1: {
                return Math.PI * (arr.get(0) * arr.get(0));
            }
            case 2: {
                return arr.get(0) * arr.get(1);
            }
        }
        return -1.0;
    }
}
