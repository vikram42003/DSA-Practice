// link - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

public class _744_Find_Smallest_Letter_Greater_Than_Target {
    public char nextGreatestLetter(char[] letters, char target) {
        int idx = -1, l = 0, r = letters.length - 1;

        // Handle egde cases here
        if (target < letters[0] || target >= letters[letters.length - 1])
            return letters[0];

        // Use binary search to look for element after target
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (letters[mid] == target) {
                idx = mid + 1;
                l = mid + 1;
            } else if (letters[mid] > target) {
                idx = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return letters[idx];
    }
}
