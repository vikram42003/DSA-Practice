from typing import List


class Solution:
    # Brute Force Solution - Time = O(n) - Space = O(1)
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (
                (i < 1 or flowerbed[i - 1] != 1)
                and flowerbed[i] == 0
                and (i >= len(flowerbed) - 1 or flowerbed[i + 1] != 1)
            ):
                n -= 1
                flowerbed[i] = 1

        return n <= 0

    # Greedy Solution - Time = O(n) - Space = O(1)
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        # Check edgecase for length == 1
        if l == 1 and flowerbed[0] == 0:
            return True
        # Check for leftmost index
        if l > 1 and flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        # Check for rightmost index
        if l > 1 and flowerbed[l - 1] == flowerbed[l - 2] == 0:
            flowerbed[l - 1] = 1
            n -= 1

        for i in range(1, l - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                i += 1

        return n <= 0
