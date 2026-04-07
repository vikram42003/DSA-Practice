class Solution:
    # Freq maps - Time = O(n) - Space = O(1)
    # Count the frequency of chars in s1 in s1freq
    # Then Count the frequency of chars in s2 within a sliding window, return True on match
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = [0] * 26
        s2freq = [0] * 26

        for s in s1:
            s1freq[ord(s) - 97] += 1

        l, r, n, m = 0, 0, len(s1), len(s2)

        while r < m:
            s2freq[ord(s2[r]) - 97] += 1
            r += 1

            if r - l > n:
                s2freq[ord(s2[l]) - 97] -= 1
                l += 1

            if all(s1freq[i] == s2freq[i] for i in range(26)):
                return True

        return False
