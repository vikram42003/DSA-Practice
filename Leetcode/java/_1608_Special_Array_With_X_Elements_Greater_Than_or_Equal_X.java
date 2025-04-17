public class _1608_Special_Array_With_X_Elements_Greater_Than_or_Equal_X {
    public int specialArray(int[] nums) {
        for (int i = 1; i <= nums.length; i++) {
            int count = 0;
            for (int j = 0; j < nums.length; j++) {
                if (i <= nums[j])
                    count++;
            }
            if (count == i)
                return i;
        }
        return -1;
    }
}
