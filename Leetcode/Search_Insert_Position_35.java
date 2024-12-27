// link - https://leetcode.com/problems/search-insert-position/description/

class Search_Insert_Position_35 {
    public int searchInsert(int[] nums, int target) {
        if (nums[nums.length - 1] < target)
            return nums.length;

        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }
}