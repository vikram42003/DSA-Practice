from typing import List


class Solution:
    # Optimal - Time = O(n) - Space = O(1)
    # Just like the Prefix/Suffix approach except instead of using arrays to track prefix suffix sums, we can see that
    # for any particular idx, we only need the leftmax and rightmax for that index, so we can keep a running lmax and rmax
    # and then compute that directly, also we had the min(prefix[i], suffix[i]), so we can do calculations based on that 
    # by just checking for lmax < rmax beforehand
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        lmax, rmax = height[l], height[r]
        res = 0
    
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]

        return res
    
    # Prefix/Suffix Sums - Time = O(n) - Space = O(n)
    # First pre-compute left and right maximum boundary heights for every index:
    #  - prefix[i] stores the max height from index 0 to i
    #  - suffix[i] stores the max height from index i to n-1
    #
    # Then iterate through each bar i to calculate trapped water:
    #  - The water level at index i is bounded by min(prefix[i], suffix[i])
    #  - Water trapped at i = water level - height[i]
    #  - Accumulate water whenever water level > height[i]
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix, suffix = [0] * n, [0] * n
        l, r = 0, n - 1
        while l < n:
            prefix[l] = max(height[l], prefix[l - 1] if l - 1 >= 0 else 0)
            suffix[r] = max(height[r], suffix[r + 1] if r + 1 < n else 0)
            l += 1
            r -= 1

        maxWater = 0

        for i in range(n):
            cur = min(prefix[i], suffix[i]) - height[i]
            if cur > 0:
                maxWater += cur

        return maxWater

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
