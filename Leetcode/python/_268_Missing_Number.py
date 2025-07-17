from typing import List


class Solution:
    # Cyclic Sort - 
    # the array has numbers from 0 to n but we sort from 1 to n,
    # the cyclic sort has a property where any duplicates or numbers not within the range accumulate at the empty spots in 
    # the list in no particular order
    # so after we place all numbers at their correct positions, 0 will be place at the index where the missing number should go
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        ans_idx = -1
        while i < len(nums):
            if nums[i] == 0:
                ans_idx = i
                i += 1
                continue

            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        return ans_idx + 1
