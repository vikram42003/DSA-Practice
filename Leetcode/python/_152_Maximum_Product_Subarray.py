from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_max, cur_max, cur_max_neg = nums[0], 1, nums[0]
        # Iterate over all numbers
        i = 0
        while i < len(nums):
            if cur_max == 0:
                cur_max = 1
            
            cur_max *= nums[i]
            max_max = max(max_max, cur_max, cur_max_neg)
            i += 1
            
            
            
            
            
            
            
            # If cur_max is 0, meaning we multiplied by 0 in prev iteration then reset cur_max to 1
            if cur_max == 0:
                cur_max = 1
            # If cur_max is negative, meaning we multiplied by a negative number in the prev iteration, then keep multiplying it with the next number until it becomes positive or if we run out of numbers
            elif cur_max < 0:
                temp = cur_max
                while i < len(nums) and temp < 0:
                    temp *= nums[i]
                    i += 1

                # We found another negative number, which makes cur_max positive
                if temp > 0:
                    cur_max = temp
                    max_max = max(max_max, cur_max)
                # We did not find another negative
                else:
                    cur_max = 1
                    max_max = max(max_max, temp)
            # Continue multiplying numbers as normal and maintaining cur_max and max_max
            else:
                cur_max *= nums[i]
                max_max = max(max_max, cur_max)
                
            i += 1
        return max_max


test = Solution()
# ans = 32
arr = [-2, 2, 2, 2, 2, -1]
print(test.maxProduct(arr))
