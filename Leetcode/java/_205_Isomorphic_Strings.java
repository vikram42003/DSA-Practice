// link - https://leetcode.com/problems/isomorphic-strings/

public class _205_Isomorphic_Strings {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() == 1 && !(s.equals(t)))
            return false;

        int[] map1 = new int[256];
        int[] map2 = new int[256];

        for (int i = 0; i < s.length(); i++) {
            if (map1[s.charAt(i)] != map2[t.charAt(i)])
                return false;
            map1[s.charAt(i)] = i + 1;
            map2[t.charAt(i)] = i + 1;
        }

        return true;
    }
}
