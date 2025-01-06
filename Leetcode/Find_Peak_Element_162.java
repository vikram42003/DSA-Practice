// link - https://leetcode.com/problems/find-peak-element/description/

public class Find_Peak_Element_162 {
    public int findPeakElement(int[] nums) {
        int l = 0, r = nums.length - 1;

        while (l <= r) {
            int mid = l + ((r - l) / 2);
            int prev = mid - 1 >= 0 ? nums[mid - 1] : Integer.MIN_VALUE;
            int next = mid + 1 < nums.length ? nums[mid + 1] : Integer.MIN_VALUE;

            if (nums[mid] > prev && nums[mid] > next) {
                return mid;
            } else if (prev > next) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return 0;
    }
}
