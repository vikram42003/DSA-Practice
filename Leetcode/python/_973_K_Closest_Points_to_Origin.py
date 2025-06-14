from heapq import heappush, heappushpop
from typing import List


class Solution:
    # Heap approach - Time = O(n + log n) -> O(n log n) - Space - O(n + k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = -(x * x + y * y)
            if len(heap) == k:
                heappushpop(heap, (dist, x, y))
            else:
                heappush(heap, (dist, x, y))

        return [(x, y) for dist, x, y in heap]
    
    # 
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for idx, p in enumerate(points):
            d = (p[0] ** 2) + (p[1] ** 2)
            dist.append((d, idx))

        def quick_select(left, right):
            low = left
            high = right
            pivot = dist[right][0]

            while low <= high:
                while dist[low][0] < pivot:
                    low += 1
                while dist[high][0] > pivot:
                    high -= 1
                if low <= high:
                    temp = dist[low]
                    dist[low] = dist[high]
                    dist[high] = temp
                    low += 1
                    high -= 1

            if k <= high:
                return quick_select(left, high)
            elif k >= low:
                return quick_select(low, right)
            else:
                res = []
                for i in range(k):
                    idx = dist[i][1]
                    res.append(points[idx])
                return res

        return quick_select(0, len(points) - 1)
