from typing import List


class Solution:
    # Monotonic Stack - Time = O(n) - Space = O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_max = 0
        # stack is an ascending monotonic stack and will store indices of the heights
        stack = []

        for i in range(len(heights) + 1):
            # After iterating over heights, we run the loop another time and set the height
            # to 0 to empty out the stack
            height = heights[i] if i < len(heights) else 0

            while stack and height < heights[stack[-1]]:
                idx = stack.pop()
                # for width
                # stack[-1] will be the leftbound for the current width for this element
                # i will be the rightbound
                # we do -1 to start counting BEFORE the left bound
                # IF stack is empty, then that means we're already at the left bound, all we need
                # is the right bound, which is just i
                width = i - stack[-1] - 1 if stack else i
                max_max = max(max_max, heights[idx] * width)

            stack.append(i)

        return max_max

    # Less Optimized Version (OLD but more clearer)
    # Monotonic Stack - Time = O(n) - Space = O(n)
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