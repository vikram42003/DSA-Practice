class Solution:
    # Iterative Fast Exponent - Time = O(log n) - Space = O(1)
    # The core idea is - 2^10 can be reduced to 4^5, so if n is even, change the goal post closer like this
    # if n is odd then just normally do * x to res and -1 to n to make it even and balanced again
    def myPow(self, x: float, n: int) -> float:
        isNeg = False
        if n < 0:
            n = -n
            isNeg = True

        res = 1
        while n > 0:
            # Even, so double x and halve n
            if (n & 1) == 0:
                x *= x
                n //= 2
            # Odd, just process a normal single multiplication of res by x
            else:
                res *= x
                n -= 1

        return 1 / res if isNeg else res

    # Fast Exponentiation - Time = O(log n) - Space = O(n)
    # 5^10 is the same as doing 5^5 * 5^5, so just do that
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n):
            if n == 0:
                return 1

            half = rec(x, n // 2)

            if n & 1:
                return half * half * x
            else:
                return half * half

        return rec(x, n) if n >= 0 else 1 / rec(x, -n)
