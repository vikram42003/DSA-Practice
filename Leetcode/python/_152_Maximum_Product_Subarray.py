from typing import List


class Solution:
    # We need to find the CONTIGUOS subarray with the largest product
    # And nums may have negatives in it
    # BUT
    #   - If there are even number of negatives in nums, then product oall elements of nums would be the product of all its elements
    #   - (considering there are no zeros in the middle, otherwise the array would be divided)
    #
    #   - If there are odd number of negatives then we need to exclude one of the negatives at and after/before the rightmost 
    #     and the leftmost negative number   
    #   - remember, we need there to be even number of negatives and we cannot remove any of the negative in the middle (cause
    #     the array needs to stay contiguos)
    
    #   - If we encounter 0 in nums then reset the counting variables
    def maxProduct(self, nums: List[int]) -> int:
        max_max = nums[0]
        ignoring_leftmost_negative = 0
        ignoring_rightmost_negative = 0
        even_negatives = 1
        
        for n in nums:
            if n == 0:
                max_max = max(max_max, ignoring_leftmost_negative, ignoring_rightmost_negative, even_negatives, 0)
                ignoring_leftmost_negative = 0
                ignoring_rightmost_negative = 0
                even_negatives = 1
            
            if n < 0:
                ignoring_rightmost_negative = even_negatives
            
            even_negatives *= n
            ignoring_leftmost_negative *= n

            if ignoring_leftmost_negative == 0 and n < 0:
                ignoring_leftmost_negative = 1

        return max(max_max, ignoring_leftmost_negative, ignoring_rightmost_negative, even_negatives)

test = Solution()
# ans = 6
arr1 = [2, 3, -2, 4]
# ans = 0
arr2 = [-2, 0, -1]
# ans = 32
arr3 = [-2, 2, 2, 2, 2, -1]
# ans = 48
arr4 = [-2, 2, 2, -2, 2, -3]
# ans = 960
arr5 = [-1, 4, -4, 5, -2, -1, -1, -2, -3]
# print(test.maxProduct(arr1))
print(test.maxProduct(arr2))
# print(test.maxProduct(arr3))
# print(test.maxProduct(arr4))
# print(test.maxProduct(arr5))
