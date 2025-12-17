class Solution:
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
