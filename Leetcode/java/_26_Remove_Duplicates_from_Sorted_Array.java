// link - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

public class _26_Remove_Duplicates_from_Sorted_Array {
    public static void main(String[] args) {
        int[] nums = { 1, 1, 2, 3, 4, 4 };
        System.out.println(removeDuplicates(nums));
    }

    public static int removeDuplicates(int[] nums) {
        int idx = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[idx] = nums[i];
                idx++;
            }
        }
        return idx;
    }
}
