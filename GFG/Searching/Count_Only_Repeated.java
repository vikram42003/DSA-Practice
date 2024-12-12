public class Count_Only_Repeated {
    // Pair Class
    static class Pair {
        long x;
        long y;

        Pair(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    // Function to find repeated element and its frequency.

    // Naive - Iterative solution
    public static Pair findRepeatingIterative(long arr[], int n) {
        // Your code here
        long count = -1, elem = -1;

        for (int i = 1; i < n - 1; i++) {
            if (arr[i] == arr[i - 1]) {
                elem = arr[i];
                if (count == -1)
                    count = 1;
                count++;
            }
        }

        Pair pair = new Pair(elem, count);
        return pair;
    }
}
