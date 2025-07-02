from collections import deque
from typing import List


class Solution:
    # (TLE) Brute Force - Time = O(n^2) - Space = O(1) 
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dist = 0
        for i in range(len(nums)):
            min_val = nums[i]
            max_val = nums[i]

            for j in range(i, len(nums)):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])

                if abs(min_val - max_val) <= limit:
                    dist = max(dist, j - i)
                else:
                    break

        return dist + 1
    
    # Two Pointers and Monotonic Deque - Time = O(n) - Space = O(n)
    # The idea is - we keep track of the current max and current min, within the subarray we're looking at cause if
    # the abs(max - min) <= limit, then that means all other elements within the subarray are also valid
    # But we need to expand or contract the subarray (TWO POINTERS), so we need a way to instantly know whats the current 
    # biggest/smallest num, second/biggest smallest and so on, and we need it to mantain its order (MONOTONIC) and we need 
    # to look at whats the current biggest/smallest instantly, add new elements to list and may need to remove the current
    # biggest/smallest too (DEQUE) 
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = deque() # Monotonic Ascending deque
        maxq = deque() # Monotonic Descending deque

        l = 0
        res = 0
        for r in range(len(nums)):
            # Make sure the queues remain monotonically asc/desc
            while minq and nums[r] < minq[-1]: minq.pop()
            while maxq and nums[r] > maxq[-1]: maxq.pop()

            minq.append(nums[r])
            maxq.append(nums[r])

            while maxq[0] - minq[0] > limit:
                if nums[l] == minq[0]: minq.popleft()
                if nums[l] == maxq[0]: maxq.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res


test = Solution()
# ans = 4
arr = [1, 3, 5, -3, 2, 4, 6, 7]
limit = 5
print(test.longestSubarray(arr, limit))
