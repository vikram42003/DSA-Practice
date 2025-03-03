// link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class _121_Best_Time_to_Buy_and_Sell_Stock {
    // Prefix/Postfix sum solution - Time = O(3n) = O(n) - Space = O(2n) = O(n)
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[] prefixArr = new int[n];
        int[] postfixArr = new int[n];

        prefixArr[0] = prices[0];
        for (int i = 1; i < n; i++) {
            prefixArr[i] = Math.min(prefixArr[i - 1], prices[i]);
        }

        postfixArr[n - 1] = prices[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            postfixArr[i] = Math.max(postfixArr[i + 1], prices[i]);
        }

        int maxDiff = 0;
        for (int i = 0; i < n; i++) {
            maxDiff = Math.max(maxDiff, postfixArr[i] - prefixArr[i]);
        }

        return maxDiff;
    }

    // Optimized solution - Time = O(n) - Space = O(1)
    // We consider each day as the buying price for the stock
    // track the changes to the price after we've bought the stock in curr and keep
    // track of the max value that curr has hit
    // if at any point curr gets negative then that means we've hit a new lower
    // point and should try buying at this price
    // return the max diff
    public int maxProfitOptimized(int[] prices) {
        int curr = 0, max = 0;
        for (int i = 1; i < prices.length; i++) {
            curr += prices[i] - prices[i - 1];
            if (curr < 0)
                curr = 0;
            max = Math.max(max, curr);
        }
        return max;
    }
}