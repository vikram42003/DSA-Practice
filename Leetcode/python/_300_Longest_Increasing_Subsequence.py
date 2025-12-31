from bisect import bisect_left
from typing import List


class Solution:
    # DP + Binary Search (Patience Sorting) - Time = O(n log n) - Space = O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State will be each possible length of the subsequence, which will have length len(nums)
        # It will store whats the minimum possible num we can end on for each possible substring value
        # Like for [10,9,2,5,3,7,101,18], tails[1] will be 2 because that forms the maximum increasing
        # substring of length 1 with the minimum ending number
        tails = []

        # (Check out Patience Sorting)
        # After that for each num, find the first position where num >= tails[i], or thinking 
        # inversely, first value where num was bigger than some tail position, that will be the 
        # position where we should repalce num with, if its within the array then replace, otherwise
        # append at the end of the array
        for num in nums:
            idx = bisect_left(tails, num)

            if idx == len(tails):
                # num is larger than all existing tails, so it extends the longest increasing subsequence
                tails.append(num)
            else:
                # num improves (lowers) the ending value of a subsequence of length idx + 1
                # no need for any min checks, this position will be >= num
                tails[idx] = num
        
        # The length of tails represents the length of the longest increasing subsequence found
        return len(tails)
    
    # DP (Bottom up tabulation) - Time = O(n ^ 2) - Space = O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp states will be the longest increasing substring for each index i
        dp = [1] * n
        max_max = 1

        # then we just pick the longest previously calculated subsequences out of all the
        # subsequences we have calculated, only if the starting point of that substring (nums[j])
        # is greater than the current element (nums[i])
        for i in range(n - 1, -1, -1):
            cur = 0
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    cur = max(cur, dp[j])
            dp[i] += cur
            max_max = max(max_max, dp[i])

        # and return the global max
        return max_max
