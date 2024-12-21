// User function Template for Java

// Input - arr[] of POSITIVE integers
//       - ascending order

// To Find - there is a SINGLE repeating element
//         - which is repeating any(2 or more) number of times

// Output - pair.x = the element, pair.y = number of times it repeats
//        - if no repeating element is found then return pair.x = -1, pair.y = -1

// Approach - Naive - Time = O(n) - Space = O(1)
//          - Just keep a counter that tracks the max number of times we've seen
//            the element, since the elements are in ascending order therefore
//            if arr[i - 1] == arr[i] then counter++ else reset counter and also
//            keep a max count
//            then just return max count and corresponding element if its greater
//            than 1 else return -1, -1

//          - Optimized using binary search - Time = O(log n) - Space = O(1)
//            if a digit is not misisng the last digit in the array will
//            be array.length so return -1, -1 if thats the case
//            otherwise
//            outOfOrderElement will be the differene between arr[n - 1] - (arr[0] + n - 1)
//            outOfOrderIndex will be the first element thats not at its correct
//            position and we can find it by doing a left bound binary search
//            and then return outOfOrderIndex and outOfOrderCount as a "Pair"

// Theory - Optimized using binary search -
//            now how would we know which one is the missing one,
//            well thats the entire question

//            here in the array arr[i] will be i + 1, like arr[0] will be 1, arr[1] = 2 and so on
//            imagine we have this array
//            1 2 2 2 3 4      arr.length = n = 6, l = 0, r = 5

//            since the array has 6 elements that means that if there was no repeating
//            then arr[n - 1] = (arr[0] + n - 1) as in arr[5] would be 6
//            BUT here arr[5] is 4 and that is 2 less than 6, that means that the repeating
//            element is taking up 2 spots, so the second value that we have to return is 2

//            (we check for arr[0] + n - 1 so that it accounts for the case when the
//            array does'nt start from 1, hereafter this calculation will just be
//            replace by the result)

//            Now all we need to do is find the first element / leftmost element that is
//            not at its right place
//            for that it'll go like this

//            1 2 2 2 3 4     l = 0, r = 5, mid = 0 + 5 / 2 = 2.5 = 2
//            arr[2] = 2 but it should be 3, so that means that the order messes up somewhere
//            towards the left of the array and the current out of order element's index is
//            outOfOrder = mid = 2

//            now the array becomes
//            1 2 . . . .     l = 0, r = 1, mid = 0 + 1 / 2 = 0.5 = 0
//            arr[0] = 1 which is correct since it should be 1 so the out of order element
//            must lie to the right so we'll look right

//            now the array becomes
//            . 2 . . . .     l = 1, r = 1, mid = 1 + 1 / 2 = 1
//            arr[1] = 2 which is also correct so the outOfOrder element must lie to the right

//            now, when we assing l = mid + 1, l = 2 then l becomes greater than r
//            that means we probably have already found the ourOfOrder element 
//            and need to break out of the loop so at this point we will return
//            outOfOrder = 2, outOfOrderCount = 2
//            which matches the answer that is [2, 2]



public class Count_Only_Repeated {
    // Pair Class
    static class Pair {
        long x;
        long y;

        Pair(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    // Function to find repeated element and its frequency.

    // Naive - Iterative solution
    public static Pair findRepeatingIterative(long arr[], int n) {
        // Your code here
        long count = -1, elem = -1;

        for (int i = 1; i < n - 1; i++) {
            if (arr[i] == arr[i - 1]) {
                elem = arr[i];
                if (count == -1)
                    count = 1;
                count++;
            }
        }

        Pair pair = new Pair(elem, count);
        return pair;
    }

    // Binary search approach
    public static Pair findRepeating(long arr[], int n) {
        // pair.x = outOfOrderElement
        // pair.y = outOfOrderCount
        Pair pair = new Pair(-1, -1);

        if (arr[n - 1] == (arr[0] + n - 1)) {
            return pair;
        } else {
            pair.y = (arr[0] + n) - arr[n - 1];
        }

        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            long num = arr[0] + mid;
            if (arr[mid] == num) {
                // the element is at its correct spot, so search the right half
                l = mid + 1;
            } else {
                // the out of order element lies to the left so search the left half
                // also keep track of the latest outOfOrder element encountered
                r = mid - 1;
                pair.x = arr[mid];
            }
        }

        return pair;
    }
}
