// link - https://leetcode.com/problems/sqrtx/

public class _69_Sqrt {
    public int mySqrt(int x) {
        if (x < 2)
            return x;
        long guess = x / 2;
        while (guess * guess > x) {
            guess = (guess + (x / guess)) / 2;
        }
        return (int) guess;
    }
}
