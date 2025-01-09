import java.util.ArrayList;
import java.util.HashMap;

public class _350_Intersection_of_Two_Arrays_II {
    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums1) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        ArrayList<Integer> result = new ArrayList<>();
        for (int num : nums2) {
            if (map.getOrDefault(num, -1) > 0) {
                result.add(num);
                map.put(num, map.get(num) - 1);
            }
        }

        int[] ans = new int[result.size()];
        int i = 0;
        for (int num : result) {
            ans[i++] = num;
        }

        return ans;
    }
}
