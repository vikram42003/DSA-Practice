from typing import List


class Solution:
    # Binary Search - Time = O(log n) - Space = O(1)
    # The core idea is - Since the array is rotated but still sorted, at any point in time, either the
    # mid to left half or the mid to right half will be sorted, so all we really gotta focus on, is whether
    # the target lies in the mid to left sorted half or the mid to right sorted half
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # Emphasis on <=, incase l and m are the same
            # This case means the left half is sorted
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # This case means the right half is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        # return -1 if target still not found
        return -1


test = Solution()

# ans = 4
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
test.search(nums, target)

# ans = 1
nums = [1, 3]
target = 3
test.search(nums, target)
