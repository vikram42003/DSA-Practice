// link - https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

public class _1752_Check_if_Array_Is_Sorted_and_Rotated {
    public boolean check(int[] nums) {
        int split = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > nums[(i + 1) % nums.length])
                split++;
        }
        return split < 2;
    }
}
