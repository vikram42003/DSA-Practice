from typing import List


class Solution:
    # DP (Bottom Up Tabulation) - Time = O(n ^ sum/2) - Space = O(sum/2)
    # The main idea is, for us to evenly split an array, it should have even sum, and if one of
    # the subarray can get a total sum of arrSum // 2, denoted by target, then the remaining part
    # would auromatically have the sum as other remaining half
    # So we run a bottom up tabulation based dp recusion in a clever way with the help of sets
    # We iterate from last num to first, and for each num, we add it to all the elements in the set
    # and store the num to the set as is as well
    # Initially we set the set as { 0 } so that it always includes num itself, and as soon as we
    # find an element that sums up to target we return True immediately
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        # If totalSum is odd then there is no way to evenly split the array
        if totalSum & 1:
            return False

        target = totalSum // 2
        dp = set([0])

        for i in range(len(nums) - 1, -1, -1):
            newDp = set()
            for d in dp:
                if nums[i] + d == target:
                    return True
                newDp.add(nums[i] + d)
                newDp.add(d)
            dp = newDp

        return False

    # DFS - Time = O(n ^ 2) - Space = O(n)
    # Can be optimized, but it was for exploring/understanding the problem, so im just gonna
    # focus on the actual optimal solution
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        a = []
        b = []

        def dfs(i):
            if i == n:
                return sum(a) == sum(b)

            # choice 1: put nums[i] in a
            a.append(nums[i])
            if dfs(i + 1):
                return True
            a.pop()

            # choice 2: put nums[i] in b
            b.append(nums[i])
            if dfs(i + 1):
                return True
            b.pop()

            return False

        return dfs(0)
