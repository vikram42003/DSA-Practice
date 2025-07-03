from collections import deque
from typing import List


class Solution:
    # Deque - Time = O(n) - Space = O(n)
    # The idea is - we add all elements to a data strcuture and that data structure must keep them in descending order (MONOTONIC)
    # and we need to move the window, so we need to remove the leftmost element on each iteration, so we need a data structure
    # that is in an order, allows us to insert elements in the list, and allows us to remove the topmost element quickly if that
    # element happens to be the leftmost element
    # So what we do is
    # - iterate over the array, add elements to the queue while mantain a descending order, once the window is size k then
    # look at the biggest element in the queue (dq[0]) and add it to result.
    # - After that move the window, and if the element that we're removing from the window happens to be the max element
    # then pop from left in the queue. We dont care about elements that we're removing that are lesser than current max element
    # since we only need to work with the max
    # - return the result!
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Monotonic descending queue
        res = []

        l = 0
        for n in nums:
            while dq and n > dq[-1]:
                dq.pop()

            dq.append(n)
            k -= 1

            if k <= 0:
                res.append(dq[0])
                if nums[l] == dq[0]:
                    dq.popleft()
                l += 1

        return res


test = Solution()
# ans = [3,3,5,5,6,7]
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# ans =
nums2 = [5, 4, 2, 1, 1]
k2 = 3
print(test.maxSlidingWindow(nums, k))
