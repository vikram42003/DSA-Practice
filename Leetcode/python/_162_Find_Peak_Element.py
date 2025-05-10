from typing import List


class Solution:
    # Naive Solution - Time = O(n) - Space = O(n)
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            prev_num = nums[i - 1] if i > 0 else float("-inf")
            next_num = nums[i + 1] if i < len(nums) - 1 else float("-inf")

            if nums[i] > prev_num and nums[i] > next_num:
                return i

        return -1
    
    # Binary Search Solution - Time = O(log n) - Space = O(1)
    def findPeakElementBinarySearch(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            prev_num = nums[mid - 1] if mid - 1 >= 0 else float("-inf")
            next_num = nums[mid + 1] if mid + 1 < len(nums) else float("-inf")

            if prev_num < nums[mid] and next_num < nums[mid]:
                return mid
            elif next_num > prev_num:
                l = mid + 1
            else:
                r = mid - 1

        return -1