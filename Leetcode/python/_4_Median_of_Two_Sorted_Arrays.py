from typing import List


class Solution:
    # Split Binary Search - Time = O(log(min(n, m))) - Space = O(1)
    # The core idea is - Median means middle elelent, for even arrays its both mid elements / 2, for odd arrays its 
    # just mid element
    # So in a normal array, we could have just found the n // 2 element, but from that we observe that we just need
    # to split both the arrays such that the left half of the nums1 + left half of nums2 have exactly n + m // 2 
    # elements (half of total length elements)
    # and both nums1Left[-1] <= nums2Right[0] and nums2Left[-1] <= nums1Right[0], to ensure its a valid half for 
    # a binary search
    # How to find where to divide? Well we do that by running a binary search over the smaller array and adjusting 
    # the bounds incase nums1Left[-1] <= nums2Right[0] is not true (meaning shrink the window over nums1)
    # Or expand the window otherwise
    # We check with <= instead of < because it doesnt need to be strictly increasing, there might be duplicates
    # We substitue out of bounds elements as -inf on the left and inf on the right
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # If nums1 > nums2 then swap them to ensure that nums1 is the smaller one, so that we run the binary
        # search on the smaller array
        n, m = len(nums1), len(nums2)
        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        total = n + m
        half = total // 2
        l, r = 0, n - 1
        while True:
            # i will be the point where we choose the rightside bound of nums1
            i = l + (r - l) // 2
            # j will be the point where we choose the rightside bound of nums2
            # We can just get this by choosing the elements remaining to make up to half of total
            j = half - i - 2  # -1 two times for zero indexing of i and j

            nLeft = nums1[i] if i >= 0 else float("-inf")
            mLeft = nums2[j] if j >= 0 else float("-inf")
            nRight = nums1[i + 1] if i + 1 < n else float("inf")
            mRight = nums2[j + 1] if j + 1 < m else float("inf")

            # If the partition is correct then return the median
            if nLeft <= mRight and mLeft <= nRight:
                if (total & 1) == 1:
                    return min(nRight, mRight)
                else:
                    return (max(nLeft, mLeft) + min(nRight, mRight)) / 2
            # If nLeft > mRight then shrink the window
            elif nLeft > mRight:
                r = i - 1
            # Otherwise expand the window
            else:
                l = i + 1
