from collections import defaultdict
from typing import List


class DetectSquares:
    # The main idea is, we keep a track of all the points and when we recieve a query, we iterate over the points
    # and find a point that is not query and is diagonal to current point, diagonal ensures that all sides are
    # equal so then we'd only have check and count if there are points at (query_x, cur_y) and (cur_x, query_y)
    # to make the diagonal a square
    def __init__(self):
        # Store the points and their count
        self.pointCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        # Add a new point and update the count
        self.pointCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0

        for x, y in self.points:
            if abs(x - qx) == abs(y - qy) and x != qx and y != qy:
                # We do multiply to ensure that the final calcualtion counts any extra overlapping points at
                # top left and bottom right
                # The overlapping points at bottom left (diagonal) are automaticall taken care of because we
                # store the points in a list and it can store duplicates
                res += self.pointCount[(x, qy)] * self.pointCount[(qx, y)]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
