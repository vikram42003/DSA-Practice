// link - https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

package GFG.Searching;

public class Kth_Element_Of_Two_Arrays {
    public int kthElement(int a[], int b[], int k) {
        // Ensure a is the smaller array
        if (a.length > b.length) {
            int[] temp = a;
            a = b;
            b = temp;
        }

        int l = Math.max(0, k - b.length), r = Math.min(a.length, k);
        while (l <= r) {
            int midA = l + ((r - l) / 2);
            int midB = k - midA;

            int a1 = midA > 0 ? a[midA - 1] : Integer.MIN_VALUE;
            int a2 = midA < a.length ? a[midA] : Integer.MAX_VALUE;
            int b1 = midB > 0 ? b[midB - 1] : Integer.MIN_VALUE;
            int b2 = midB < b.length ? b[midB] : Integer.MAX_VALUE;

            if (a1 <= b2 && b1 <= a2) {
                return Math.max(a1, b1);
            } else if (a1 > b2) {
                r = midA - 1;
            } else {
                l = midA + 1;
            }
        }

        return -1;
    }
}
