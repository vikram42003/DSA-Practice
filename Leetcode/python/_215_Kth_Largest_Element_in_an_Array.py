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

    # Counting Occurences Approach - Time = O(n) - Space = O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)

        count = [0] * (max_val - min_val + 1)

        for n in nums:
            count[n - min_val] += 1

        for i in range(len(count) - 1, -1, -1):
            k -= count[i]
            if k <= 0:
                return i + min_val

    # Quick Selection Approach - Time = Θ(n) and O(n^2) - Space = O(1) - TLE!!! (need to partition into 3 for it to work within time limit)

    # Here we use the concept used in selection part of selection sort
    # Also, here we'll sort the list in ascending order
    # We need to find the kth largest element, if we sort the list in ascending order, thats the (len(nums) - k) element from the right
    # We take a pivot (rightmost element in this case) and the sort the list according to that
    # iterate from left -> if nums[i] < pivot then swap it with index j and increment j, if nums[i] > pivot then leave it alone
    # after iterating swap pivot with nums[j], now EVERY ELEMENT to the left of nums[j] is smaller than it, and every element to
    # its right is bigger than it, in other words we can say that it is GUARENTEED that nums[j] is at its correct position
    # Now if j == k then we've found the element, if j < k then we need to do this same operation to the left of the list, otherwise
    # we need to do it to the right of the list
    # do that until j == k and we would have found the kth largest element

    # NOTE - if the array is already in ascending order like - [1, 2, 3, 4, 5] then the time complexity of the algorithm will
    # be n^2 cause we'll have to eliminate the rightmost element one by one while checking each element (n - eliminated elementes) times
    # BUT in average case it'll be O(n) cause on average we'll sort roughly half the list, elminate either left or right half, sort it again
    # and then eliminate the other half again and again until we find the kth element. So time complexity will be n + n/2 + n/4 + n/8 + ...
    # and so on and that is mathematically equal to 2n

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        l, r = 0, len(nums) - 1

        def quick_select(l: int, r: int):
            cur = l
            pivot = nums[r]

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[cur] = nums[cur], nums[i]
                    cur += 1

            nums[cur], nums[r] = nums[r], nums[cur]

            if cur == k:
                return nums[cur]
            elif cur < k:
                return quick_select(cur + 1, r)
            else:
                return quick_select(l, cur - 1)

        return quick_select(l, r)


test = Solution()
arr = [3, 2, 1, 5, 6, 4]
print(test.findKthLargest(arr, 2))
