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
                max_max = max(
                    max_max,
                    ignoring_leftmost_negative,
                    ignoring_rightmost_negative,
                    even_negatives,
                    0,
                )
                ignoring_leftmost_negative = 0
                ignoring_rightmost_negative = 0
                even_negatives = 1

            if n < 0:
                ignoring_rightmost_negative = even_negatives

            even_negatives *= n
            ignoring_leftmost_negative *= n

            if ignoring_leftmost_negative == 0 and n < 0:
                ignoring_leftmost_negative = 1

        return max(
            max_max,
            ignoring_leftmost_negative,
            ignoring_rightmost_negative,
            even_negatives,
        )

    # Kadane Algo - Time = O(2n) - Space = O(1)
    #
    # You see the idea in the explanation above right
    # Let me summarize again
    # only positive numbers or even negatives == ╰(*°▽°*)╯
    # Odd negatives                           == (┬┬﹏┬┬)
    # So we gotta ignore either the leftmost or the rightmost negative and the numbers before/after that (cant ignore a negative
    # in the middle cause, it gotta be a contiguos subarray and longer == better)
    # SO LETS RUBN A GFUFKING LIOP FROM LEGT AND RIGHT AND KEEP TRACKIGN MAX_MAX AND TEHN RETURN IT AND WE GOOD
    # If the prod gets reset or becomes negative it gets auto ignored
    # And if there are odd negatives then the normal loop will (effectively) ignore rightmost negative and beyond, and the reverse
    # loop will ignore the leftmost negative and before
    def maxProduct(self, nums: List[int]) -> int:
        max_max = nums[0]
        prod = 1

        for i in range(len(nums)):
            prod *= nums[i]
            max_max = max(max_max, prod)
            if prod == 0:
                prod = 1

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            max_max = max(max_max, prod)
            if prod == 0:
                prod = 1

        return max_max
    
    # Dymanic Programming - Time = O(n) = Space - O(1)
    # We keep track of the maximum and the minimum product of the subarray we're considering till now, because if we encounter a
    # negative that can turn our maximum product to minimum and minimum product to maximum, so we keep track of that while also
    # keeping track of what our global max is
    # Also we dont need to do anything special for n == 0 because if n == 0 then "(n * max_val, n * min_val, n)" or "(tmp, n * min_val, n)"
    # would all be (0, 0, 0) effectively resetting all values, and in the next loop max_val val and min_val would be set to n
    def maxProduct(self, nums: List[int]) -> int:
        max_max = nums[0]
        max_val, min_val = 1, 1

        for n in nums:
            tmp = n * max_val
            max_val = max(n * max_val, n * min_val, n)
            min_val = min(tmp, n * min_val, n)
            max_max = max(max_max, max_val)

        return max_max


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
