from typing import List


class Solution:
    # Greedy Solution - Time = O(n log n + m log m) = O(n log n) - Space = O(1) (Although it can be O(n) in 
    # a very miniscule number of cases due to python sort method using Timsort under the hood)
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1

        return count
