// link - https://www.geeksforgeeks.org/problems/second-largest3735/1

package GFG;

public class Second_Largest {
    public int getSecondLargest(int[] arr) {
        int max = Integer.MIN_VALUE;
        int secMax = Integer.MIN_VALUE;

        for (int i : arr) {
            if (i > max) {
                secMax = max;
                max = i;
            } else if (i > secMax && i < max) {
                secMax = i;
            }
        }

        if (secMax == Integer.MIN_VALUE) {
            return -1;
        }

        return secMax;
    }
}
