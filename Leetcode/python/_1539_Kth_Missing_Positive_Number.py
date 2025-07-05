from typing import List


class Solution:
    # Linear Search - Time = O(n) - Space = O(1)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k

        idx = 0
        num = 0
        while idx < len(arr) and k > 0:
            num += 1
            if num == arr[idx]:
                idx += 1
            else:
                k -= 1

        return num if k < 0 else num + k
