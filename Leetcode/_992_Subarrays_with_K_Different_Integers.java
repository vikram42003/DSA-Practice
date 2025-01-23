// link - https://leetcode.com/problems/subarrays-with-k-different-integers/

import java.util.HashMap;

public class _992_Subarrays_with_K_Different_Integers {
    public static void main(String[] args) {
        int[] nums = { 1, 2, 1, 2, 3 }; // ans = 7
        int k = 2;

        int[] nums2 = { 1, 2 }; // ans = 2?
        int k2 = 1;

        int[] nums3 = { 2, 1, 1, 1, 2 }; // ans = 8
        int k3 = 1;

        System.out.println(subarraysWithKDistinct(nums3, k3));
    }

    public static int subarraysWithKDistinct(int[] nums, int k) {
        int total = 0;
        HashMap<Integer, Integer> map = new HashMap<>();

        int near = 0, far = 0;
        for (int right = 0; right < nums.length; right++) {
            map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);

            while (map.size() > k) {
                map.put(nums[near], map.getOrDefault(nums[near], 0) - 1);
                map.remove(nums[near], 0);
                near++;
                far = near;
            }

            while (map.getOrDefault(nums[near], 0) > 1) {
                map.put(nums[near], map.getOrDefault(nums[near], 0) - 1);
                near++;
            }

            if (map.size() == k) {
                total += near - far + 1;
            }
        }

        return total;
    }

    // Was trying to do a 3 pointer approach by my own intuition but it didnt really
    // work out
    // Maybe try making this work when you revisit this problem
    public static int subarraysWithKDistinctFailedAttempt(int[] nums, int k) {
        int total = 0;
        HashMap<Integer, Integer> map = new HashMap<>();

        int near = 0, far = 0;
        for (int right = 0; right < nums.length; right++) {
            map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);

            if (map.size() < k) {
                continue;
            } else if (map.size() == k) {
                while (map.get(nums[near]) > 1) {
                    map.put(nums[near], map.get(nums[near]) - 1);
                    near++;
                }
                total += near - far + 1;
            } else {
                map.clear();
                map.put(nums[right], 1);

                near = right;
                while (near >= 0 && map.size() < k) {
                    near--;
                    map.put(nums[near], map.getOrDefault(nums[near], 0) + 1);
                }

                total++;
                far = near;
            }
        }

        return total;
    }
}
