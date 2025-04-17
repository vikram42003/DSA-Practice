// link - https://leetcode.com/problems/valid-anagram/description/

import java.util.HashMap;

public class _242_Valid_Anagram {

    // Naive Solution - Time = O(n) - Space = O(1);
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] letters = new int[26];
        for (int i = 0; i < s.length(); i++) {
            letters[s.charAt(i) - 'a']++;
            letters[t.charAt(i) - 'a']--;
        }
        for (int i : letters)
            if (i != 0)
                return false;

        return true;
    }

    // Naive Solution - Time = O(3n) - Space = O(n);
    public boolean isAnagramLessOptimized(String s, String t) {
        HashMap<Character, Integer> hashMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            hashMap.put(c, hashMap.getOrDefault(c, 0) + 1);
        }
        for (char c : t.toCharArray()) {
            if (!hashMap.containsKey(c))
                return false;
            hashMap.put(c, hashMap.get(c) - 1);
        }
        for (int i : hashMap.values()) {
            if (i != 0)
                return false;
        }

        return true;
    }
}
