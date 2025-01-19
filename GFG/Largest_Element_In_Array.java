// link - https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0

package GFG;

public class Largest_Element_In_Array {
    public static int largest(int[] arr) {
        int max = Integer.MIN_VALUE;
        for (int i : arr) {
            max = Math.max(max, i);
        }
        return max;
    }
}
