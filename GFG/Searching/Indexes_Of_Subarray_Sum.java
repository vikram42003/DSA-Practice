// link - https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

// Question - Given an unsorted array arr containing only non-negative 
//           integers, your task is to find a continuous subarray 
//           (a contiguous sequence of elements) whose sum equals a 
//           specified value target. You need to return the 1-based 
//           indices of the leftmost and rightmost elements of this 
//           subarray.

// Input - int[] arr
//       - unsorted
//       - only positive integers (0 included)

// Constraints - arr.length >= 1 
//             - arr[i] = 10 ^ 3 (within int range)
//             - target = 10 ^ 9 (within int range)

// Output - leftmost and rightmost indices of a contiguous subarray
//        - where subarray sum is equal to target
//        - RETURN ANSWER AS 1 BASED INDEX
//        - return -1 if no answer is found

// Example - int[] arr = { 1, 2, 3, 7, 5 }   target = 12
//         - output = [2, 4] because the sum of elements 2 + 3 + 7 = 12
//           and the elements are contiguous

// Approach - sliding window on array - Space = O(1) - Time = O(n) -
//            - run a for loop through the array and start adding it to sum
//            - create a variable j that points to the start of the list
//            - if sum > target then start deducting arr[j] from sum, incrementing
//              j on each step while i <= j && sum > target
//            - after that check if sum == target and return if true else keep the for
//              loop going
//            - return -1 if we cannot find an answer

import java.util.ArrayList;

class Indexes_Of_Subarray_Sum {

    public static void main(String[] args) {
        // TESTING AND DEBUGGING
        int[] arr = { 38, 22, 20, 12, 47, 23, 18, 13, 18, 47, 36, 42 };
        int target = 174;

        int[] arr1 = { 1, 2, 3, 7, 5 }, arr2 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }, arr3 = { 7, 2, 1 },
                arr4 = { 5, 3, 4 }, arr5 = { 19, 23, 15, 6, 6, 2, 28, 2 };
        int target1 = 12, target2 = 15, target3 = 2, target4 = 2, target5 = 2;

        // 0 = 7,12 --- 1 = 2,4 --- 2 = 1,5 --- 3 = 2,2 --- 4 = -1 --- 5 = 6,6

        System.out.println(subarraySum(arr, target));
        System.out.println(subarraySum(arr1, target1));
        System.out.println(subarraySum(arr2, target2));
        System.out.println(subarraySum(arr3, target3));
        System.out.println(subarraySum(arr4, target4));
        System.out.println(subarraySum(arr5, target5));
    }

    static ArrayList<Integer> subarraySum(int[] arr, int target) {
        ArrayList<Integer> list = new ArrayList<>();

        int j = 0, sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];

            while (sum > target && j <= i) {
                sum -= arr[j];
                j++;
            }

            if (sum == target) {
                list.add(j + 1);
                list.add(i + 1);
                return list;
            }
        }

        list.add(-1);
        return list;
    }
}
