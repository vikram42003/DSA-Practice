from typing import List


class Solution:
    # Cyclic Sort - Time = O(2n) = O(n) - Space = O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] < 1 or nums[i] > len(nums):
                i += 1
                continue
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[correct], nums[i] = nums[i], nums[correct]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


# Working Notes

# # Apporach ? - Time = O(n) - Space = O(n)
# take max and min (non negative)
# create a boolean array of size max - min
# interate over array and mark present elements true
# iterate over boolean array and return first element not present

# # Approach ??
# iterate over array and mark i - 1 th element somehow

# # Approach ???
# cyclic sort the array, ignore elements out of range [1, n)
# iterate from i = 0 to len(nums) and return the first case where nums[i] != i + 1
# if we go through the whole list that means list is like this [1, 2], and the missing element is
# len(nums) + 1
