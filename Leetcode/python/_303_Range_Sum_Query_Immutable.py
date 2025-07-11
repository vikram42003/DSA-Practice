from typing import List


class NumArray:

    # Time = O(n * c) - Space = O(1)
    # n - number of elements, c - number of times we call run the for loop for each sumRange call
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
