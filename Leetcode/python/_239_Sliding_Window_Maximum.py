from collections import deque
import heapq
from typing import List


class Solution:
    # Heap - Time = O(n log k) - Space = O(n)
    # We create a heap, which will store the descending list of elements and their indices, and we'll lazily check for validity 
    # of the top value. From that I mean, before adding the top element, we'll check if it lies outside the range of the current
    # window, and if it does, remove it in a while loop until we reah an element that is the max element within the bounds
    # of the current window
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Add first k element to the max heap
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res = [-heap[0][0]]

        for i in range(k, len(nums)):
            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)            
            heapq.heappush(heap, (-nums[i], i))
            res.append(-heap[0][0])

        return res
    
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
