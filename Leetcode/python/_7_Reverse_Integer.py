class Solution:
    def reverse(self, x: int) -> int:
        maxVal, minVal = 2**31 - 1, -(2**31)
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0
        while x > 0:
            num = x % 10
            x //= 10

            if res > (maxVal - num) // 10:
                return 0

            res = res * 10 + num

        res *= sign
        return res if minVal <= res <= maxVal else 0
