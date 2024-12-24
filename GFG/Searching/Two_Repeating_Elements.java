// Question - You are given an integer n and an integer array arr of size
//           n+2. All elements of the array are in the range from 1 to n.
//           Also, all elements occur once except two numbers which occur
//           twice. Find the two repeating numbers. Note: Return the
//           numbers in their order of appearing twice. So, if x and y
//           are repeating numbers, and x's second appearance comes
//           before the second appearance of y, then the order should be
//           (x, y).

// Input - int[] arr = array of integers
//       - arr[i] or each array element is <= n
//       - arr.length = n + 2
//       - n = int value >= 2

// Output - int[] result = [repeating element 1, repeating element 2]
//        - return the repeating elements in the order of their occurence

// Constraints - n is >= 2 and <= 100000 (within int range)
//             - arr[i] is >= 1 and <= n (equal to or smaller than n
//               and within int range)

// Observations - since the array is not sorted, cant use binary search
//                and there might be a better way than sorting and then binary
//                searching

// Approach - Negative marking elements - Time = O(n) - Space = O(1)
//            since we know that each element of the array is greater than 0
//            and less than or equal to n
//            We can conclude that all elements of the array will be within
//            the array index range
//            And we can use that to mark each element on position "arr[i]"
//            as negative, and if it is already marked negative that means that
//            this is the second time we encounter this element so its the
//            repeating element.
//            Furthermore, this ensures that we are adding the elements in the
//            order of the encounter of their duplicate

class Two_Repeating_Elements {
    // Function to find two repeated elements.
    public int[] twoRepeated(int n, int arr[]) {
        // Your code here
        int[] ans = new int[2];
        int idx = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[Math.abs(arr[i])] < 0) {
                ans[idx] = Math.abs(arr[i]);
                idx++;
            }
            arr[Math.abs(arr[i])] *= -1;
        }

        return ans;
    }
}