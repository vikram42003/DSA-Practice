from heapq import heapify, heappop
from typing import List


class Solution:
    # Heap Approach - Time = O(n log n) - Space = O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapify(heap)
        for i in range(k - 1):
            heappop(heap)
        return -1 * heap[0]

    # Sorting Approach - Time = O(n log n) - Space = O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]
