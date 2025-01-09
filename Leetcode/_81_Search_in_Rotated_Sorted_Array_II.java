// link - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

public class _81_Search_in_Rotated_Sorted_Array_II {
    public boolean search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while (l <= r) {
            int mid = l + ((r - l) / 2);

            if (nums[mid] == target) {
                return true;
            } else if (nums[l] == nums[r]) {
                l++;
            } else if (nums[l] <= nums[mid]) {
                if (target >= nums[l] && target < nums[mid]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else {
                if (target <= nums[r] && target > nums[mid]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }

        return false;
    }
}
