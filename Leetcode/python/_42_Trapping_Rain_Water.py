from typing import List


class Solution:
    # Sweep Left and Right - Time = O(n) - Space = O(1)
    # The core idea is - we can traverse from left to right, take a left bound as a wall, once we
    # have a wall, we see if current height < left wall, if yes then left wall - the height of the elevation
    # at the current element is the potential amount of water that can accumulate here, keep that up until
    # we hit a height >= left wall, at which point we "close" the container and dump all the accumulated
    # potential water into totalWater, then reset and continue with the new wall.
    #
    # BUT here's the annoying caveat, what if we NEVER hit a wall tall enough to close it?
    # Which means that once we're at an element that is strictly > than all the elements to the left of it
    # we wont be able to track any water after it.
    # To handle that, we can just simply track where the peak is and then do the same sweep we've been doing
    # from right upto peak this time
    # Go until RIGHTMOST PEAK INCASE THEYRE DUPLICATES, END AT PEAK TO PREVENT DOUBLE COUNTING
    def trap(self, height: List[int]) -> int:
        totalWater, leftHeight, potentialWater = 0, 0, 0
        peak, peakIdx = 0, -1

        for i, h in enumerate(height):
            if h >= peak:
                peak = h
                peakIdx = i

            if h < leftHeight:
                # if current height < leftHeight then water can potentially accumulate here, but also
                # reduce the spots filled with blocks
                potentialWater += leftHeight - h
            else:
                totalWater += potentialWater
                leftHeight = h
                potentialWater = 0

        rightHeight, potentialWater = 0, 0
        for i in range(len(height) - 1, peakIdx - 1, -1):
            if height[i] < rightHeight:
                potentialWater += rightHeight - height[i]
            else:
                totalWater += potentialWater
                rightHeight = height[i]
                potentialWater = 0

        return totalWater


test = Solution()
# ans = 6
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(test.trap(arr))
