from typing import List


class Solution:
    # Cycle Sort - Time = O(2n) - Space = (d)
    # d = duplicates in the array
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicates.append(nums[i])

        return duplicates

    # Like Cyclic Sort but flip signs instead of sorting - Time = O(n) - Space = O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0:
                duplicates.append(abs(n))
            else:
                nums[i] *= -1

        return duplicates
