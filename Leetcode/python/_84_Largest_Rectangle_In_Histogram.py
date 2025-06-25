from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_max = 0
        # stack is an ascending monotonic stack and will store pair of values
        stack = [] # pair = (index, height)

        for i in range(len(heights)):
            idx = i
            while stack and heights[i] < stack[-1][1]:
                val = stack.pop()
                max_max = max(max_max, (i - val[0]) * val[1])
                idx = val[0]
            stack.append((idx, heights[i]))

        while stack:
            val = stack.pop()
            max_max = max(max_max, (len(heights) - val[0]) * val[1])

        return max_max