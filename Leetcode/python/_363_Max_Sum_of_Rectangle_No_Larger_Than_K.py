from typing import List

from sortedcontainers import SortedList


class Solution:
    # Loop from col[0] to end, then col[1] to end and so on
    # Compress the 2D array into a 1D one, prefix summing all elements before the current columm
    # and store the values for each corresponding row in temp
    # Now the value at each row is the value of a rectange that has a width of idx 0 to current
    # element and height of 1, all we need to do now is find out how many other contiguos
    # rectangles we can combine, in other words the height of the rectangle, while keeping
    # its total value under k

    # The problem is essentially "largest subarray sum less than K" at this point
    # And to solve that we can use make use of prefix sum and apply a similar method to two sum
    # iterate over temp and keep a running prefix sum, if prefix sum exceeds k, the check whats
    # the smallest possible part of the subarray from the left we can exclude to get our
    # running prefix sum back under k
    # like if temp = [3, 2, 5, 9] and k = 10
    # 19 - x <= 10   9 <= x   x >= 9
    # when we reach index 3, runningSum will be 19 which is > k, so how many elements from
    # the left do we need to exclude ?
    # 19 - toRemove <= 10   9 <= toRemove   toRemove >= 9
    # we need the sum of those elements to be >= 9 so we'll remove elements form idx 0 to 2
    # then runningSum will be less than k
    # Do this for each element while recording what gets runningSum closest to k and
    # Return that answer!
    # We will use TreeSet or SortedList for log n insertion of prefix sums at each index and log n lookup of the first prefix sum >= runningSum - k

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        max_max = float("-inf")
        # The 2 outermost loops will run less number of times compared to the inner "2D to 1D conversion" loop
        # So make sure matrix has less columns than rows
        rows, cols = len(matrix), len(matrix[0])
        if rows < cols:
            matrix = list(zip(*matrix))
            rows, cols = cols, rows

        for left in range(cols):
            temp = [0] * rows
            for right in range(left, cols):
                for i in range(rows):
                    temp[i] += matrix[i][right]

                runningSum = 0
                # We initialize the list with 0, so that when runningSum == k but and then we
                # search for 0 in prefixSums, then we do find a match and update max_max
                prefixSums = SortedList([0])

                for n in temp:
                    runningSum += n
                    i = prefixSums.bisect_left(runningSum - k)
                    if i < len(prefixSums):
                        max_max = max(max_max, runningSum - prefixSums[i])
                    # Early exit
                    if max_max == k:
                        return k
                    prefixSums.add(runningSum)

        return max_max

print("test")