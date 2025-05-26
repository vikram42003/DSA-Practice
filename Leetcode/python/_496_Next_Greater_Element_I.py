from typing import List


class Solution:
    # Brute Force -
    # Just linear search nums1[i] in nums2, and then move right until end or elem > nums1[i] is found
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in nums1:
            found = False
            num = -1

            for j in nums2:
                if i == j:
                    found = True
                elif found and j > i:
                    num = j
                    break

            res.append(num)

        return res
