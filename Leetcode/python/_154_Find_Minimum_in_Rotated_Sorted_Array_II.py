from typing import List


class Solution:
    # Binary Search Approach - Time = O(n log n) - Space = O(1)
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            while r > l and nums[l] == nums[r]:
                r -= 1

            mid = l + (r - l) // 2

            if nums[l] < nums[r]:
                break
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
    
    # Optimized Binary Search Approach - Time = O(n log n) - Space = O(1)
    def findMinOptimized(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
            
        return nums[l]
