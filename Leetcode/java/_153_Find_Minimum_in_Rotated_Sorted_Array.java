// link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

public class _153_Find_Minimum_in_Rotated_Sorted_Array {
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = l + ((r - l) / 2);
            if (nums[mid] > nums[r]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return nums[l];
    }
}
