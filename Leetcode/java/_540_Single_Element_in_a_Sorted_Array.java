// link - https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class _540_Single_Element_in_a_Sorted_Array {
    public int singleNonDuplicate(int[] nums) {
        int l = 0, r = nums.length - 1;

        while (l <= r) {
            int mid = l + ((r - l) / 2);

            int prev = mid - 1 >= 0 ? nums[mid - 1] : -1;
            int next = mid + 1 <= nums.length - 1 ? nums[mid + 1] : -1;

            if (nums[mid] != prev && nums[mid] != next) {
                return nums[mid];
            } else if (((mid & 1) == 1 && prev == nums[mid]) || ((mid & 1) == 0) && next == nums[mid]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return -1;
    }
}