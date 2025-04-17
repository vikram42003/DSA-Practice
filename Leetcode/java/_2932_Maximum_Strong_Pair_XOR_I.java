// link - https://leetcode.com/problems/maximum-strong-pair-xor-i/

public class _2932_Maximum_Strong_Pair_XOR_I {
    // Brute force solution
    public int maximumStrongPairXor(int[] nums) {
        int max = 0;

        for (int i : nums) {
            for (int j : nums) {
                if (Math.abs(i - j) <= Math.min(i, j)) {
                    max = Math.max(max, i ^ j);
                }
            }
        }

        return max;
    }
}
