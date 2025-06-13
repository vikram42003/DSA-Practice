// link - https://leetcode.com/problems/search-in-rotated-sorted-array/description/

public class _33_Search_in_Rotated_Sorted_Array {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while (l <= r) {
            int mid = l + ((r - l) / 2);

            if (nums[mid] == target) {
                return mid;
            } else if (nums[l] <= nums[mid]) {
                if (target >= nums[l] && target < nums[mid]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else {
                if (target > nums[mid] && target < nums[l]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }

        return -1;
    }
}
