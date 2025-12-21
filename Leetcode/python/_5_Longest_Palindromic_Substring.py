class Solution:
    # Manacher's Algorithm - Time = O(n) - Space = O(n)
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
    def longestPalindrome(self, s: str) -> str:
        # Put # between each letter and the boundaries so that the total length is always consistent
        pal = "^#" + "#".join(s) + "#$"
        n = len(pal)
        # Length will track the span of the palindrome starting from each letter
        length = [0] * n

        # c will track the center of the biggest palindrome we've seen till now, r will track its right boundary
        c = r = 0
        for i in range(1, n - 1):
            # First find the index of element that mirrors current element i
            mirror = 2 * c - i

            # If the current index we're checking is within the span of the current biggest palindrome
            # found, then we can depend on the mirror property of a palindrome, and this ensures that
            # either the minimum of the remaining part from i to r, or the length of palindrome
            # originating from current elements mirror, will be the same
            if i < r:
                length[i] = min(r - i, length[mirror])

            # Start expanding from the next unknown index
            while pal[i - length[i] - 1] == pal[i + length[i] + 1]:
                length[i] += 1

            # If we find a bigger r boundary then update it
            if i + length[i] > r:
                c = i
                r = i + length[i]

        # In the end we'll find the biggest palindrome center, convert its dimensions for the original
        # string, and return that substring
        max_len = max(length)
        center = length.index(max_len)
        start = (center - max_len) // 2
        return s[start : start + max_len]

    # Expand Around Center - Time = O(n^2) - Space = O(1)
    # For each letter expand around it until you find a mismatching corresponding character and track the max
    # While expanding the palindrome could start at a single character ("bob") or two characters ("lool")
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        for i in range(n):
            # Check for one char center palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if len(res) < r - l + 1:
                    res = s[l : r + 1]
                l -= 1
                r += 1

            # Check for two char center palindromes
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if len(res) < r - l + 1:
                    res = s[l : r + 1]
                l -= 1
                r += 1

        return res
