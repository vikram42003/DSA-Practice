from typing import Counter


class Solution:
    # The core idea is - instead of comparing each char in t to each char in the current window,
    # we can instead count if current s[r] count matches the required count for that character at
    # s[r] in t (or well countT)
    # If s[r] in window is exactly equal, then we have the required number of count for that char
    # If s[r] in window is > required, we can ignore that, we already have all the count for s[r] we need
    # Once we have all the needed chars then we can start shrinking the window, and have will only
    # decrease once the chars we have for s[l], the one we just removed, fall below required
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = Counter(t), {}
        # Initialize countT to UNIQUE chars, cause have and need will count which unqiue chars have been satisfied, their counts are tracked by countT and window
        have, need = 0, len(countT)
        startIdx, endIdx, length = -1, -1, float("inf")
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < length:
                    length = r - l + 1
                    startIdx, endIdx = l, r

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return s[startIdx : endIdx + 1] if length != float("inf") else ""
