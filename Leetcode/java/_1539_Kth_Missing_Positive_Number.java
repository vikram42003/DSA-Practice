// link - https://leetcode.com/problems/kth-missing-positive-number/description/

// if arr[0] > k then ans = k;
// so what if we move the index to be a number that is greater than k
// then we can just say that k is the answer
// like this
// arr[] = { 4, 5, 6, 10 }   k = 3
// here since arr[0] which is 4 is greater than 3 then the answer is 3
// BUT what if we were asked 5th missing number
// to find the 5th missing number the current number that we are checking
// must obviously be greater than 5 right
// so in the array lets take arr[2] which is 6
// BUT this cannot be the answer because 4 and 5 are already in the array so
// we cannot say that 5 is the missing number
// So that means whenever we check an element, we gotta account for the elements
// that are before it, and since the array is sorted this makes it easier
// So the actual value of arr[i] becomes arr[i] - i - 1 
// (doing -1 since an array is 0 indexed)
// So at arr[2] = 6 - 2 - 1 = 3 that means 3 elements are missing at array position 2
// But we need the fifth missing element so while doing a binary search we will look
// at the right half
// Now we get to arr[3] = 10 - 3 - 1 = 6 so 6 elements are missing before 10
// So to find the missing number we will do 10 - (6 - k - 1) = 10 - 2 = 8
// (The equation can be simplified to m + k, i did the math on a white board to 
// arrive at this conclustion and you can do that too to confirm it
// Additionally it can be further simplified to l + k, because when we find the leftmost
// number that gets us the result then the left pointer will point to the last/final
// result while only the right one will be moving)
// and then store the result and look left to see incase we have missed the correct
// result
// then return the result

class _1539_Kth_Missing_Positive_Number {
    public static void main(String[] args) {
        int[] arr = { 2, 3, 4, 7, 11 }; // ans = 9
        int k = 5;

        System.out.println(findKthPositive(arr, k));
    }

    public static int Naive_findKthPositive(int[] arr, int k) {
        // Naive solution - hash and iterate
        boolean[] someName = new boolean[arr[arr.length - 1] + 1];
        for (int i = 0; i < arr.length; i++) {
            someName[arr[i]] = true;
        }
        for (int i = 1; i < someName.length; i++) {
            if (!someName[i])
                k--;
            if (k == 0)
                return i;
        }
        return arr[arr.length - 1] + k;
    }

    public static int findKthPositive(int[] arr, int k) {
        // Binary search solution
        if (arr[0] > k) {
            return k;
        } else if (arr[arr.length - 1] < k) {
            return k + arr.length;
        }

        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (arr[mid] - mid - 1 >= k) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return l + k;
    }
}