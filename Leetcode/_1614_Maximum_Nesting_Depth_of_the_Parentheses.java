// link - https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

public class _1614_Maximum_Nesting_Depth_of_the_Parentheses {
    public int maxDepth(String s) {
        int max = 0;
        int curr = 0;
        for (char c : s.toCharArray()) {
            if (c == '(')
                curr++;
            if (c == ')')
                curr--;
            max = Math.max(curr, max);
        }
        return max;
    }
}
