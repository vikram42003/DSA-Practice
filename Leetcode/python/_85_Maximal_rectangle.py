from typing import List


class Solution:
    # 2D Kadane Algo Appraoch - Time = O(n*(m^2)) - Space = O(n)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_max = 0

        # We iterate over each col in the matrix
        # This outer loop's goal is kind of find out the starting column or the left boundary
        # of the biggest rectangle
        for left in range(len(matrix[0])):
            # We already know we need to apply kadane, but kadane cannot work on a 2D array, so
            # we kinda need to flatten the rows, which we can do by keeping a prefix sum for each
            # row and invalidating the row by adding a value like -100, if we run into a 0, since
            # that row should not be included
            # temp will serve as our flat row
            temp = [0] * len(matrix)

            # Iterate from the left boundary to the end of matrix and mantain a prefix sum
            # for each row of the current column
            for right in range(left, len(matrix[0])):
                # Iterate over each row
                for row in range(len(matrix)):
                    val = matrix[row][right]
                    if val == "1":
                        temp[row] += 1
                    else:
                        temp[row] = -100

                # Now each positive element in the temp is the number of 1's without any 0's in
                # that row
                # We basically have the width of our rectangle, and we need to find the height
                # which will be the subset of temp with the largest consecutive sum of values
                # And for that the perfect algorithm is Kadane's

                curr = 0
                for i in temp:
                    if curr < 0:
                        curr = 0
                    curr += i
                    max_max = max(max_max, curr)

        return max_max


test = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(test.maximalRectangle(matrix))
