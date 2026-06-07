from typing import List


class Solution:
    # Binary Search - Time = O(n log n) - Space = O(1)
    # The core idea is, that instead of simulating the splitting, we instead binary search for the
    # minimum penalty value (using the bisect binary search template)
    # The min could be 1, and the max could be the max element in nums
    # And for the conditon, we iterate through nums and then see how many operations we need to get the
    # current element <= to the min penality we've chosen for this iteration (lets call this x)
    # And then count the number of operations, with o += math.ceil(n / x)
    # And if o exceeds the maxOperations then this x value is not possible, and so on
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def condition(x):
            o = 0
            for n in nums:
                if n > x:
                    # This is equivalent to math.ceil(n / x) - 1 but faster
                    o += (n - 1) // x
                    if o > maxOperations:
                        return False
            return True

        l, r = 1, max(nums) + 1
        while l < r:
            m = l + (r - l) // 2
            if condition(m):
                r = m
            else:
                l = m + 1
        return l
