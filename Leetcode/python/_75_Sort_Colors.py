from typing import List


class Solution:
    # Bubble Sort - Time = O(n^2) - Space = O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            swapped = False
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break

    # Dutch National Flag (3 Way Sort) - Time = O(n) - Space = O(1)
    # The basic idea is that we divide the array into 3 sections, since the array values can only
    # be 0, 1, 2. So iterate over the array with i, if current element is a 0, put it at the left end
    # and if it is 2 then put it at the right end, doing that, 1 will automatically be at its
    # correct place, and we're done
    # One thing to note is that we're going from left to right, so if i == 2, then it would be moved
    # to the right so we can say there are no 2s to the left of i, since we'd have moved it already
    # So if we swap left and i, the new element at i WILL be a 1 so doing i += 1 after that would just
    # be efficient
    # but the right side may have 0, 1, 2 cause its unexplored, so if we swap from right, the new
    # element at i could be 0 or 1 or 2, so imagine if it was 0 and we did i += 1 then we'd mess up
    # the order, so dont increment i if we swap from right
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, i, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1
