// link - https://leetcode.com/problems/divide-array-into-equal-pairs/

import java.util.HashMap;

public class _2206_Divide_Array_Into_Equal_Pairs {
    public boolean divideArray(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        for (int i : map.values()) {
            if ((i & 1) == 1)
                return false;
        }

        return true;
    }
}
