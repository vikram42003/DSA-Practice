// Approach 1 - Binary Search each array
// - do firstNegative(arr[i]) for each array item
// - sum the total
// - return the result
// Time - O(n log n)   Space - O(1)

class Count_Negative_Numbers_in_a_Sorted_Matrix_1351 {
    public static void main(String[] args) {
        int[][] arr = { { 4, 2, 1, 1, -2 } }; // ans = 3;
        int[][] arr2 = {
                { 4, 3, 2, -1 },
                { 3, 2, 1, -1 },
                { 1, 1, -1, -2 },
                { -1, -1, -2, -3 }
        }; // ans = 8
        int[][] arr3 = { { 3, 2 }, { 1, 0 } }; // ans = 0

        System.out.println(countNegatives(arr3));
    }

    public static int countNegatives(int[][] grid) {
        int count = 0;
        for (int[] arr : grid) {
            int negative = firstNegativeIndex(arr);
            if (negative != -1) {
                count += arr.length - firstNegativeIndex(arr);
            }
        }
        return count;
    }

    public static int firstNegativeIndex(int[] arr) {
        int l = 0, r = arr.length - 1;
        while (l < r) {
            int mid = l + ((r - l) / 2);
            if (arr[mid] <= -1) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l < arr.length && arr[l] < 0 ? l : -1;
    }
}
