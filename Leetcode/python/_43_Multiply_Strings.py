class Solution:
    # IRL Math Multiplication logic + array - Time = O(n * m) - Space = O(n + m)
    def multiply(self, num1: str, num2: str) -> str:
        if "0" == num1 or "0" == num2:
            return "0"

        n, m = len(num1), len(num2)
        # Max length the product can take is n * m, Eg. 99 * 99 is 9801
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # Multiply the number at this digit's place
                prod = int(num1[i]) * int(num2[j])
                # In the multiplication table you write when doing the actual multiplication
                # The offset for where this prod should go is the number of times the bottom number
                # is leftward, that is the base + the number of times the top number is leftward
                # Here the correct idx is i + j + 1 because the size of res is n + m, and i + j is
                # initialized with two -1s, so the valid index in that case would be i + j + 1
                res[i + j + 1] += prod
                # Handle the carry, if overflow
                res[i + j] += res[i + j + 1] // 10
                # Handle the remaining if we moved the carry on overflow
                res[i + j + 1] %= 10

        # Skip leading zeros
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        # Make each int a str
        ans = map(str, res[start:])
        # join and return the result
        return "".join(ans)

    # Cheese Solution, likely not whay they intend from you, also slower than optimal
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        n, m = len(num1), len(num2)
        for j in range(m - 1, -1, -1):
            for i in range(n):
                res += (int(num1[i]) * (10 ** (n - i - 1))) * (
                    int(num2[j]) * (10 ** (m - j - 1))
                )
        return str(res)
