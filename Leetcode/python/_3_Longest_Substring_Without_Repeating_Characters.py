class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        seen = set(s[0])
        max_len = 1

        i, j = 0, 1
        while j < len(s) and i < j:
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_len = max(max_len, len(seen))
            j += 1

        return max_len
