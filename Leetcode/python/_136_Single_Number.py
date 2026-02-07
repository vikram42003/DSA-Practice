from typing import List


class Solution:
    # XOR - Time = O(n) - Space = O(1)
    # The core idea is - if we xor [2,2], result will be 0, for [2,1,2,1] - 2^1=3, 3^2=1, 1^1 = 0
    # So as long as there are pairs of two, ans will be 0, but if a singular one were to enter the fray
    # the it'll be carried over till the end and will be the answer
    def singleNumber(self, nums: List[int]) -> int:
        cur = 0
        for n in nums:
            cur ^= n
        return cur
