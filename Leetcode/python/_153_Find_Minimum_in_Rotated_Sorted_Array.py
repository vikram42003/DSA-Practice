from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + ((r - l) // 2)

            if nums[l] <= nums[r]:
                return nums[l]
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
    
    # Most optimized version
    # The essence of binary search is dividing lists into 2 parts, as long as we can confidently divide it into 2 without 
    # error, we dont need to think of anything else
    # So here, we know that the list is sorted in ascending order, which means
    #   - nums[l] < nums[mid]
    #   - nums[mid] < nums[r]
    # either one of these or both
    # If we find out that nums[mid] > nums[r], it means the list is sorted, and that means that the smallest element that
    # should've been at the leftost index of the list, is now at the right, we dont know where, but we do know its at the right
    # And at the very least its at nums[mid] + 1 position, because we can already see that nums[r] is smaller than nums[mid]
    # Otherwise, it gotta be either the current element or towards the left
    # And thats all the information we need to know to make the decision to divide the list, binary search will do the rest
    # Also, if we're checking a rotated partition of the list (i.e. nums[mid] > nums[r]) then we'll set l = mid + 1
    # so by the end of the binary search, we'll DEFINITELY end on an unsorted partition of the list, and in here,
    # l will ALWAYS point at the smallest element of this partition, which is also the smallest element of the entire list
    def findMinOptimized(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]


test = Solution()
# ans = 1
nums = [3, 1, 2]
test.findMin(nums)