from typing import List


class Solution:
    # Cyclic Sort - Time = O(n) - Space = O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []

        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(i + 1)

        return ans
