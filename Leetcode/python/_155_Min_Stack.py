from collections import defaultdict
from heapq import heappop, heappush


class MinStack:
    # Single array with tuples - Time = O(1) - Space = O(n)
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

class MinStack:
    def __init__(self):
        self.stack = []
        self.counter = defaultdict(int)
        self.minHeap = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.counter[val] += 1
        heappush(self.minHeap, val)

    def pop(self) -> None:
        poppedVal = self.stack.pop()
        self.counter[poppedVal] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        while self.minHeap and self.counter[self.minHeap[0]] < 1:
            heappop(self.minHeap)
        return self.minHeap[0]

class MinStack:
    # Two Arrays - Time = O(1) - Space = O(n)
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or value < self.minStack[-1][0]:
            self.minStack.append([value, 1])
        elif value == self.minStack[-1][0]:
            self.minStack[-1][1] += 1

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
            if self.minStack[-1][1] == 0:
                self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
