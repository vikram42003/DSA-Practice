from heapq import heappush, heappushpop
import random
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

    # (Not optimal) Quick Select - Time = Θ(n) and O(n^2) - Space = O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        dist = []
        for idx, p in enumerate(points):
            d = (p[0] ** 2) + (p[1] ** 2)
            dist.append((d, idx))

        def quick_select(left, right):
            low = left
            high = right
            pivot = dist[right][0]

            while low <= high:
                while low <= high and dist[low][0] < pivot:
                    low += 1
                while low <= high and dist[high][0] > pivot:
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

    # Quick Select (Hoare) in-place - Time = Θ(n) and O(n^2) - Space = O(1)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        def dist(i):
            return points[i][0] ** 2 + points[i][1] ** 2

        def partition(l, r):
            pivot = random.randint(l, r)
            pivot_dist = dist(pivot)

            low, high = l, r

            while True:
                while dist(low) < pivot_dist:
                    low += 1
                while dist(high) > pivot_dist:
                    high -= 1
                
                if low >= high:
                    return high
                
                points[low], points[high] = points[high], points[low]
                low += 1
                high -= 1
            
        l, r = 0, len(points) - 1
        target = k - 1

        while l < r:
            split = partition(l, r)

            if target == split:
                break
            elif target < split:
                r = split
            else:
                l = split + 1

        return points[:k]



test = Solution()
# ans = [[0, 1], [1, 0]]
# arr = [[0, 1], [1, 0]]
# k = 2
# ans = [[-2, 2]]
arr2 = [[1, 3], [-2, 2]]
k2 = 1
# print(test.kClosest(arr, k))
print(test.kClosest(arr2, k2))
