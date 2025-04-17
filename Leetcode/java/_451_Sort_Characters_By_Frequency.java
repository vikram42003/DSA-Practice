// link - https://leetcode.com/problems/sort-characters-by-frequency/

import java.util.Arrays;
import java.util.HashMap;

public class _451_Sort_Characters_By_Frequency {

    // HashMap and List/Array sorting approach - Time = O(n log n) - Time = O(n)
    public String frequencySort(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        Character[] counter = new Character[map.size()];
        int i = 0;
        for (char c : map.keySet()) {
            counter[i++] = c;
        }

        Arrays.sort(counter, (a, b) -> map.get(b) - map.get(a));

        StringBuilder str = new StringBuilder();
        for (char c : counter) {
            int j = map.get(c);
            while (j-- > 0)
                str.append(c);
        }

        return str.toString();
    }
}
