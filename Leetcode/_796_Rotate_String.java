// link - https://leetcode.com/problems/rotate-string/

public class _796_Rotate_String {
    // Using nested loop approach - Time = O(n^2) - Space = O(1)
    public boolean rotateStringLessMemory(String s, String goal) {
        if (s.length() != goal.length())
            return false;

        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < goal.length(); j++) {
                if (s.charAt((i + j) % s.length()) != goal.charAt(j))
                    break;
                if (j + 1 == goal.length())
                    return true;
            }
        }

        return false;
    }

    // Using combined string approach - Time = O(n) - Space = O(n)
    public boolean rotateStringQuick(String s, String goal) {
        return s.length() == goal.length() && (s + s).contains(goal);
    }
}
