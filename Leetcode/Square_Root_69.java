public class Square_Root_69 {
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
