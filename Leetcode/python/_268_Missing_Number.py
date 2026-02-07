from typing import List


class Solution:
    # The array will contain numbers for 0 to n, but one number will be missing
    # If the array were to contain all nums from [0, n] the the sum wouldve been the sum of all nums from [0, n]
    # But if one num was missing then the snum would be sum([0, n]) - missing_num
    # So we can just sum up numbers from 0 to n, and sum up all the numbers present in nums, and then the
    # difference between (sum up numbers from 0 to n) and (sum up all the numbers present in nums) will be the ans
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        cur_sum = 0
        _sum = 0
        for i in range(n):
            cur_sum += nums[i]
            _sum += i

        _sum += n

        return _sum - cur_sum

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
