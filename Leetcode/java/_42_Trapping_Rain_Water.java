// link - https://leetcode.com/problems/trapping-rain-water/

public class _42_Trapping_Rain_Water {
    // Two pointers approach - Time = O(n) - Space = O(1)
    public int trap(int[] height) {
        if (height.length <= 2) return 0;

        int l = 0, r = height.length -1;
        int leftHeight = height[l], rightHeight = height[r];
        int total = 0;

        while (l < r) {
            if (leftHeight < rightHeight) {
                l++;
                leftHeight = Math.max(leftHeight, height[l]);
                total += leftHeight - height[l];
            } else {
                r--;
                rightHeight = Math.max(rightHeight, height[r]);
                total += rightHeight - height[r];
            }
        }

        return total;
    }
}
