// link - https://leetcode.com/problems/longest-repeating-character-replacement/

import java.util.HashMap;

public class _424_Longest_Repeating_Character_Replacement {
    public static void main(String[] args) {
        String s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF";
        int k = 4; // ans = 7

        System.out.println(characterReplacement(s, k));
    }

    public static int characterReplacement(String s, int k) {
        // Find the maximum occuring character
        // This element will be the one with which we'll try to make the biggest
        // consecutive subarray
        char maxOccuring = '.';
        int maxCount = 0;

        for (char c : s.toCharArray()) {
            if (maxCount == 0) {
                maxOccuring = c;
                maxCount++;
            } else if (c == maxOccuring) {
                maxCount++;
            } else {
                maxCount--;
            }
        }

        // We'll use sliding window
        // We'll find the biggest window which has the maximum number of maxOccuring
        // character + k elements
        // We also include k here because we can change k to maxOccuring
        // l and r will denote the beginning and end of the window
        int l = 0, r = 0;
        int window = k;
        int total = 0;
        int max = k;

        // This hashmap will help us keep track of what and how many elements we have
        // in our window
        HashMap<Character, Integer> map = new HashMap<>();

        // Keep moving r and adding element at r until we hit the end of string s
        while (r < s.length()) {
            map.put(s.charAt(r), map.getOrDefault(s.charAt(r), 0) + 1);
            total++;
            window = k + map.getOrDefault(maxOccuring, 0);

            // if we exceed the maximum window then start making it smaller
            while (total > window) {
                int count = map.getOrDefault(s.charAt(l), 0);
                if (count <= 0) {
                    map.remove(s.charAt(l));
                } else {
                    map.put(s.charAt(l), count - 1);
                }
                total--;
                l++;
                window = k + map.getOrDefault(maxOccuring, 0);
            }

            max = Math.max(max, total);
            r++;
        }

        return max;
    }
}
