// link - https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

public class _1010_Pairs_of_Songs_With_Total_Durations_Divisible_by_60 {
    public static void main(String[] args) {
        int[] time = { 30, 20, 150, 100, 40 }; // ans = 3

        System.out.println(numPairsDivisibleBy60(time));
    }

    // Naive Solution - Time = O(n^2) - Space = O(1) - (Exceeds time limit)
    public int numPairsDivisibleBy60Naive(int[] time) {
        int total = 0;

        for (int i = 0; i < time.length; i++) {
            for (int j = i + 1; j < time.length; j++) {
                if ((time[i] + time[j]) % 60 == 0)
                    total++;
            }
        }

        return total;
    }

    // Optimized solution
    public static int numPairsDivisibleBy60(int[] time) {
        int[] pairs = new int[60];
        int total = 0;
        for (int i : time) {
            int rem = i % 60;
            if (rem == 0) {
                total += pairs[0];
            } else {
                total += pairs[60 - rem];
            }
            pairs[rem]++;
        }
        return total;
    }
}
