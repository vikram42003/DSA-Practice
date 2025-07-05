from typing import List


class Solution:
    # Linear Search Solution - Time = O(n) - Space = O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums), 2):
            if i + 1 >= len(nums) or nums[i] != nums[i + 1]:
                return nums[i]
        return -1
