import heapq


# 2 Heaps - Time = O(log n) - Space = O(n)
# We are essentially gonna divide the list into two sorted halves in non decreasing order with two heaps -
# 1) Left Heap will be a max heap because we need to check the rightmost element for mantaining
# the order or calculating median
# 2) Right Heap will be a min heap because we need to check its leftmost element for aforementioned reasons
# With leftHeap[0] being <= rightHeap[0], and the heaps will be approximately the same size. And we'll
# balance the heaps whenever we add an element
# First check if the heaps mantain the leftHeap[-1] being <= rightHeap[0] order, if not the pop from
# left and push to right in a while loop
# Then, If the size of heaps differs by more than one element then move the top from min/max heap to the other
# Lastly, for calculating median, if lenghts of heaps is not equal then there are odd number of
# elements so return that from left or right heap, otherwise there are even elements so return
# (leftHeap[0] + rightHeap[0]) // 2
class MedianFinder:

    def __init__(self):
        # Left Heap will be a max heap because we need to check the rightmost element for
        # mantaining the order or calculating median
        self.leftHeap = []
        # Right Heap will be a min heap because we need to check its leftmost element for
        # aforementioned reasons
        self.rightHeap = []

    def addNum(self, num: int) -> None:
        # Add the element to the left heap by default
        heapq.heappush(self.leftHeap, -num)

        # Move elements from left to right if leftHeap[-1] = rightHeap[0]
        while (
            self.leftHeap and self.rightHeap and -self.leftHeap[0] > self.rightHeap[0]
        ):
            temp = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, temp)

        # Balance the heap lengths
        if len(self.leftHeap) - len(self.rightHeap) > 1:
            temp = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, temp)
        elif len(self.leftHeap) - len(self.rightHeap) < -1:
            temp = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -temp)

    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        elif len(self.leftHeap) < len(self.rightHeap):
            return self.rightHeap[0]
        else:
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# (TLE) Naive - Append & Sort - Time = (n log n) - Space = O(n)
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()

        l = len(self.arr)
        if l & 1 == 0:
            return (self.arr[l // 2] + self.arr[(l - 1) // 2]) / 2
        else:
            return self.arr[l // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
