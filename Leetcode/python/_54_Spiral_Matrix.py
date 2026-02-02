from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bot, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []

        while top <= bot and left <= right:
            # Add top row then move down
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            # add right col then move left
            for i in range(top, bot + 1):
                res.append(matrix[i][right])
            right -= 1
            # if top is still <= bot, add bot row then move up
            if top <= bot:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bot][j])
                bot -= 1
            # If left is still <= right, add left col then move right
            if left <= right:
                for i in range(bot, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
