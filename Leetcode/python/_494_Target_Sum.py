from typing import List


class Solution:
    # DP (Math + Bottom Up 0/1 Knapsack) - Time = O(n * P) - Space = O(P)

    # taking nums = [1,1,1,1,1] and target 3 as example
    # Let P be the sum of all positive numbers and N be the sum of all negative numbers from the nums array
    # now to form target, the equation will be
    # P - N = target
    # Example - out of nums P consists of [1,1,1,1] and N [1] then P - N will be 4 - 1 = 3 == target

    # Another thing to note is P + N would just sum up to sum(nums), denoted by S
    # Example - out of nums P consists of [1,1,1,1] and N [1] then P + N will be 4 + 1 = 5 == sum(nums)

    # Adding both equations we get
    # P - N + P + N = target + S
    # 2P = target + S
    # P = (target + S) / 2

    # An edge case to consider is if S + target is odd, then it will become a fraction on division
    # with 2, and since nums contains only integers, we can't form a decimal and wont be able to get
    # a valid answer
    # Another edge case is if abs(target) > S, then we just cant reach it even by summing all nums

    # So all we really need to do is find the subsets of nums that sum up to P, and thats it!

    # For that we just do it like 0/1 knapsack, since we need to use each element exactly once, so we
    # also iterate backwards to not reuse an element

    # Note - If num = 0 then it can be in P or N, both give the same sum, but they are different
    # expressions so should be counted separately, which this code will do
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        if abs(target) > S or ((target + S) & 1) == 1:
            return 0

        P = (target + S) // 2
        dp = [0] * (P + 1)
        dp[0] = 1

        for num in nums:
            for i in range(P, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[P]

    # DP (Top Dowm Memo) - Time = O(len(nums) * sum(nums)) = O(n * n) - Space = O(len(nums) * sum(nums)) = O(n * n)
    # Just cache the dfs, for each nums[i] we can add it to cur as either negative or positive, in the end if cur == target, thats
    # a valid way so return 1, else its not so return 0
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def rec(i, cur):
            if i >= len(nums):
                return 1 if cur == target else 0
            if (i, cur) in memo:
                return memo[(i, cur)]

            memo[(i, cur)] = rec(i + 1, cur + nums[i]) + rec(i + 1, cur - nums[i])
            return memo[(i, cur)]

        return rec(0, 0)


test = Solution()
# ans = 5
nums = [1, 1, 1, 1, 1]
target = 3
print(test.findTargetSumWays(nums, target))
