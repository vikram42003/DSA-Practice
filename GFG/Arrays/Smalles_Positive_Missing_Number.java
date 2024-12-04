// Q - find the smallest positive number missing from the array

// I - integer array arr[]
//     - positive or negative numbers only
//     - repetition allowed

// C - arr.size() = within int range
//     - arr[i] size = within int range

// EX - arr[] = [ 2, -3 ,4, 1, 1, 7]
//     - find 1, we have 1
//     - find 2, we have 2
//     - find 3, 3 not found so return 3

//     - brute force (array) T(O(n^2)) S(O(1)) - 
//     - iterate over array arr.size() times untill we either find the num or dont find it

//     - bit more optimized (hash set) T(O(n)) S(O(n)) -
//     - iterate over array once, put each num in a HashSet and find largest num
//     - go from 1 to largest num, if hashSet.contains() is true then else return current num 

//     - more optimized (hash set) T(O(n)) S(O(n)) -
//     - elimiate the need for largest number and run loop from arr.length times
//     starting from 1. If the array is like [1, 2, 3, 4, 5] then it wont return
//     anything during the loop so return arr.length + 1 BUT if it skips any number
//     from 1 to arr.length then we will catch it within the loop

//     - if we dont find it return (it appears there will always be a valid solution)

// O - int (smallest missing num) only

import java.util.HashSet;

class Solution {
    // Function to find the smallest positive number missing from the array.
    public int missingNumber(int[] arr) {
        // Your code here
        HashSet<Integer> set = new HashSet<>();
        for (int i : arr) {
            set.add(i);
        }
        for (int i = 1; i <= arr.length; i++) {
            if (!set.contains(i))
                return i;
        }
        return arr.length + 1;
    }
}