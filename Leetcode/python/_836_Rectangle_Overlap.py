from typing import List


class Solution:
    # https://leetcode.com/problems/rectangle-overlap/solutions/8519984/solution-by-la_castille-a7g0
    # Interval Overlap Trick - Time = O(1) - Space = O(1)
    # Break this problem down into finding out the overlap between intervals on the x axis and the y axis
    # For lines a -> b and c -> d, there is an overlap if a < b or c < d, apply this to both axes (look at the pic in the link)
    # And return True if both axes are forming overlaps
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        X1, Y1, X2, Y2 = rec2

        return (x1 < X2 and X1 < x2) and (y1 < Y2 and Y1 < y2)
