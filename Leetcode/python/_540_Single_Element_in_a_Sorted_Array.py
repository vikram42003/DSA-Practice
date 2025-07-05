from typing import List


class Solution:
    # Linear Search Solution - Time = O(n) - Space = O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums), 2):
            if i + 1 >= len(nums) or nums[i] != nums[i + 1]:
                return nums[i]
        return -1

    # Binary Search Solution - Time = O(log n) - Space = O(1)
    # nums = [1,1,2,3,3,4,4,8,8]
    # If we observe the array we see that it is sorted and if all elements repeated 2 times then we'll see a pattern,
    # where all even indices have their corresponding repeating element at the odd index next to it - for (even) nums[0] = 1
    # its repeating pair is at (odd) nums[1]
    # So it should follow this pattern throughout the array , but somewhere along the way the element that does not repeat breaks
    # this pattern, so we check the array using binary search and see where it breaks the pattern, if the pattern is not broken
    # the non-repeating element must be to the right, if the pattern is broken the it must be to the left,
    # And once we reach an element thats not equal to its prev or next element, return that element cause thats the answer
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            next_val = nums[m + 1] if m + 1 < len(nums) else -1
            prev_val = nums[m - 1] if m - 1 >= 0 else -1

            if prev_val != nums[m] != next_val:
                return nums[m]
            elif ((m & 1) == 0 and nums[m] != next_val) or (
                (m & 1) == 1 and nums[m] != prev_val
            ):
                r = m - 1
            else:
                l = m + 1
        return -1
