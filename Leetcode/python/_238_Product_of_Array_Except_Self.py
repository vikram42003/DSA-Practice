from typing import List


class Solution:
    # Space Optimized Prefix and Suffix sums - Time = O(n) - Space = O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # This will give us prefix product for each element offset/delayed by 1
        # basically res[i] will be product of all elements of nums from 0 to i - 1
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # This will multiply the offset prefix product by offset suffix product
        # so then we'll basically be doing prefix product for i - 1 * suffix product
        # for i + 1
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

    # Prefix and Suffix sums - Time = O(n) - Space = O(2n)
    # Core idea is - for [a, b, c, d, e] if we want to get the product for all elements except c, then we'd have to do
    # a * b * d * e, or all before c (a * b) and all after c (d * e), and how do we quickly get product of all before and
    # after the current element? by keeping a prefix and a suffix sum!
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        i, j = 1, n - 2
        prefix[0] = nums[0]
        suffix[n - 1] = nums[n - 1]
        while i < n:
            prefix[i] = nums[i] * prefix[i - 1]
            suffix[j] = nums[j] * suffix[j + 1]
            i += 1
            j -= 1

        res = []
        for i in range(n):
            prev = prefix[i - 1] if i - 1 >= 0 else 1
            nxt = suffix[i + 1] if i + 1 < n else 1
            res.append(prev * nxt)

        return res
