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



    # Prefix Sum - Time = O(n * 1) - Space = O(n)
    # n - for calculating prefix sums, 1 - for each sumRange call
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pref = [0] * len(nums)
        self.pref[0] = nums[0]
        for i in range(1, len(nums)):
            self.pref[i] = nums[i] + self.pref[i - 1]
        print(self.pref)

    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right] if left == 0 else self.pref[right] - self.pref[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
