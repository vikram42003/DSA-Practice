// link - https://leetcode.com/problems/remove-outermost-parentheses/

public class _1021_Remove_Outermost_Parentheses {
    public String removeOuterParentheses(String s) {
        int count = 0;
        StringBuilder res = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c == '(')
                count++;
            if (count > 1)
                res.append(c);
            if (c == ')')
                count--;
        }

        return res.toString();
    }
}
