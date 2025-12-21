class Solution:
    # Manacher's Algorithm (Counting Variant) - Time = O(n) - Space = O(n)
    # This is an optimized version of expand-around-center that avoids redundant comparisons
    # by reusing palindrome information through symmetry.
    #
    # We first transform the string by inserting separators (#) so that all palindromes
    # have odd length, allowing uniform handling of even and odd palindromes.
    #
    # While iterating, we maintain the center (c) and right boundary (r) of the rightmost
    # palindrome found so far. If the current index lies within this boundary, we can
    # initialize its palindrome radius using the mirrored index across c, clamped by r.
    #
    # We then expand only beyond the known boundary, ensuring each character is compared
    # at most once overall, which guarantees linear time complexity.
    # 
    # After computing the palindrome radius array p[], each p[i] represents how
    # far a palindrome centered at i can expand in the transformed string.
    # Because every two units of expansion correspond to one real palindrome
    # in the original string, the number of palindromic substrings contributed
    # by center i is (p[i] + 1) // 2. Summing this over all centers gives the answer.
    def countSubstrings(self, s: str) -> int:
        text = "^#" + "#".join(s) + "#$"
        n = len(text)
        p = [0] * n

        r = c = 0
        for i in range(1, n - 1):
            mirror = 2 * c - i
            if i < r:
                p[i] = min(r - i, p[mirror])
            while text[i + p[i] + 1] == text[i - p[i] - 1]:
                p[i] += 1
            if i + p[i] > r:
                r = i + p[i]
                c = i

        total = 0
        for i in range(2, n - 2):
            total += (p[i] + 1) // 2

        return total
