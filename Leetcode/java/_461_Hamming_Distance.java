// link - https://leetcode.com/problems/hamming-distance/

public class _461_Hamming_Distance {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}
