package GFG.Arrays;

class Betting_Game {
    static int betBalance(String result) {
        int sum = 4;
        int betAmt = 1;
        for (char c : result.toCharArray()) {
            if (sum < betAmt)
                return -1;

            if (c == 'W') {
                sum += betAmt;
                betAmt = 1;
            } else if (c == 'L') {
                sum -= betAmt;
                betAmt *= 2;
            }
        }

        return sum;
    }
}