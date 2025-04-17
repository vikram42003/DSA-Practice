// link - https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

// Approach 1 - Binary Search each array - Time = O(n log n) - Space = O(1)
// - do firstNegative(arr[i]) for each array item
// - sum the total
// - return the result

// Approach 2 - Walk the staircase - Time = O(n + m) - Space = O(1)
// - start from either top-right or bottom-left corner
// - check if its negative
// - if its negative then all the items below it will also be negative, 
//   add that to sum and move one place to the right because all elements to the current column and left will be negative
// - if its not negative keep moving down until we find a negative or hit the end of the matrix
// - we will only decrease m and/or increase n
//   because if we are at arr[x][m] and its negative then no element before m will be negative,
//   the negative ones will only lie after it
//   similarly if we are at arr[n][x] then no element will lie to the left of n

class _1351_Count_Negative_Numbers_in_a_Sorted_Matrix {
    public static void main(String[] args) {
        // int[][] arr = { { 4, 2, 1, 1, -2 } }; // ans = 3;
        int[][] arr2 = {
                { 4, 3, 2, -1 },
                { 3, 2, 1, -1 },
                { 1, 1, -1, -2 },
                { -1, -1, -2, -3 }
        }; // ans = 8
        // int[][] arr3 = { { 3, 2 }, { 1, 0 } }; // ans = 0

        System.out.println(countNegativesStaircase(arr2));
    }

    public static int countNegatives(int[][] grid) {
        // Binary Search each array approach
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

    public static int countNegativesStaircase(int[][] grid) {
        // Staircase approach
        int count = 0;
        int n = 0, m = grid[0].length - 1;
        while (n < grid.length && m >= 0) {
            if (grid[n][m] < 0) {
                count += grid.length - n;
                m--;
            } else {
                n++;
            }
        }
        return count;
    }
}
