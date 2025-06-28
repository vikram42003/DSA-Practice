from typing import List


class Solution:
    # Flatten matrix and Monotonic Stack - Time = O(n*m) - Space = O(m)
    
    # We kind go top to botton row by row, adding up values in each column, if a column at
    # the current level contains 0 then set the whole row to 0, else increment column value 
    # by 1, and find biggest rect in histogram in each loop
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_max = 0
        cols = [0] * len(matrix[0])

        for row in matrix:
            for i in range(len(row)):
                if row[i] == "1":
                    cols[i] += 1
                else:
                    cols[i] = 0

            max_max = max(max_max, self.biggestRectInHist(cols))

        return max_max

    def biggestRectInHist(self, cols: List[int]) -> int:
        n = len(cols)
        max_max = 0
        stack = []

        for i in range(n + 1):
            height = cols[i] if i < n else 0

            while stack and height < cols[stack[-1]]:
                idx = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                max_max = max(max_max, cols[idx] * width)

            stack.append(i)

        return max_max
    
    
    # Less Efficient (Older)
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
