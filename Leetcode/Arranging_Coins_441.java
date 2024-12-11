// link - https://leetcode.com/problems/arranging-coins/submissions/1432718986/

class Arranging_Coins_441 {
    // Iterative solution 
    public int arrangeCoins(int n) {
        int count = 0;
        while (n >= 0) {
            count++;
            n -= count;
        }
        return count - 1;
    }
}