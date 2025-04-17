// link - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

public class _1790_Check_if_One_String_Swap_Can_Make_Strings_Equal {
    public boolean areAlmostEqualMoreEfficient(String s1, String s2) {
        int count = 0, i = -1, j = -1;
        for (int k = 0; k < s1.length(); k++) {
            if (s1.charAt(k) != s2.charAt(k)) {
                count++;
                if (i == -1)
                    i = k;
                else if (j == -1)
                    j = k;
            }
        }

        if (count == 0) {
            return true;
        } else if (count == 2 && s1.charAt(i) == s2.charAt(j) && s1.charAt(j) == s2.charAt(i)) {
            return true;
        } else {
            return false;
        }
    }

    public boolean areAlmostEqual(String s1, String s2) {
        char toFind = '_';
        int pos = -1;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                pos = i;
                toFind = s2.charAt(i);
            }
        }

        if (pos == -1) {
            return true;
        }

        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) == toFind) {
                char[] swapped = s1.toCharArray();
                char temp = swapped[i];
                swapped[i] = swapped[pos];
                swapped[pos] = temp;

                String str = new String(swapped);
                if (str.equals(s2)) {
                    return true;
                }
            }
        }

        return false;
    }
}
