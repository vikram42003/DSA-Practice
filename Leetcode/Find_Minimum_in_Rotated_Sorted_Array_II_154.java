// link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

public class Find_Minimum_in_Rotated_Sorted_Array_II_154 {
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;

        while (l < r) {
            int mid = l + ((r - l) / 2);

            if (nums[mid] > nums[r]) {
                l = mid + 1;
            } else if (nums[mid] < nums[r]) {
                r = mid;
            } else {
                r--;
            }
        }

        return nums[l];
    }
}