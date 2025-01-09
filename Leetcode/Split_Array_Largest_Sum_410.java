// To do - given an int array 'nums' and some 'k' value, split nums into k subarrays so that
//         - there are k non-empty subarrays
//         - lagrest sum of any subarray is minimized
//         then return the minimum possible subarray sum
//         (array must be split contiguously)

// Input - int[] nums - nums.length = [1 to 1000]
//       - int nums[i] - [0 to 1e6(10^6)]
//       - int k - [1 to min(50, nums.length)]
//       (means that k will either be >= 1 and <= 50 AND >= nums.length)

// Output - int result - minimum possible sum of the subarray with largest sum

// Observations - no need to do an edge case check for k > nums.length since k >= nums.length at least
//              - problem appears to be a min-of-max/max-of-min binary search
//              !!! there might be an int overflow problem when summing so do care for that
//              (addendum: did not need any long type, all tests passes with int as datatype)

// Approach - min-of-max/max-of-min type Binary Search 
//          - Time = O(n log n) 
//            - or O((k log s) + n) where k is the given k value and s is the sum of nums 
//              and n is the first initial loop to find the sum
//          - Space = O(1)

//          - we have to find the minimum possible largest subarrays sum, so lets assume
//            that this number is 'x' for now
//          - the largest possible sum that any subarray may have must be the sum of array
//            lets take that as 'r'
//          - the smallest possible sum that any subarray may have must be the largest element
//            in the array, lets take that as 'l'
//          - So we know that the answer must lie between r and l (inclusively) so now we
//            can just run a binary search with l and r and check if we can split the array 
//            into k parts while the sum of any subarray does not exceed the 'mid' value
//          - We can check for each mid value, if the check results to true then that means
//            the smallest possible sum is either this one or less that this one, so we do
//            r = mid
//          - if check results to false then that means that its not possible with this mid
//            value and we need to find a number greater than this one, so we do
//            l = mid + 1
//          - we run this loop until l < r (since we are doing r = mid, l < r wont miss any
//            number)
//          - At the end l will land upon the answer and we can just return it

class Split_Array_Largest_Sum_410 {
    public int splitArray(int[] nums, int k) {
        int l = 0, r = 0;
        for (int num : nums) {
            l = Math.max(l, num);
            r += num;
        }

        while (l < r) {
            int mid = l + ((r - l) / 2);

            if (check(mid, nums, k)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    public boolean check(int mid, int[] nums, int k) {
        int curr = 0;
        for (int num : nums) {
            curr += num;
            if (curr > mid) {
                curr = num;
                k--;
            }
        }
        k--;
        return k >= 0;
    }
}