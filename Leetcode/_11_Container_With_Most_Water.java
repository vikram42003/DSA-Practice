// link - https://leetcode.com/problems/container-with-most-water/

public class _11_Container_With_Most_Water {
    public int maxArea(int[] height) {
        int max = 0;

        int l = 0, r = height.length - 1;
        while (l < r) {
            int dist = r - l;
            int min = Math.min(height[l], height[r]);
            int curr = dist * min;
            max = Math.max(max, curr);

            if (height[l] > height[r]) {
                r--;
            } else {
                l++;
            }
        }

        return max;
    }
}
