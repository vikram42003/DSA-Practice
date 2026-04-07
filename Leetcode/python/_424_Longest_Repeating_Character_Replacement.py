class Solution:
    # Sliding window and counting frequency in Dict - Time = O(n) - Space = O(1)
    # The core idea is - we need to see if the current window of elements has ONLY x number of same + k number of replacable elements
    # First we need to mantian a window of elements, this window can be of max size Max Occuring Element + k elements we can replace
    # And we also need a frequency map, a dict, and we need to count the max occuring element, we can just calculate this on the fly
    # Then as we slide through the array, put r into the freq map, see whats the max occuring element within this window with maxOccElem = max(maxOccElem, freq[s[r]]) and then see if the window size - max occ has a maximum of only k different elements, if not then we remove elements from the left, otherwise this is a valid window that has subsequent elements + k replaced elements so then track and update the maxLegth variable
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        maxLength = 0
        maxOccElem = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxOccElem = max(maxOccElem, freq[s[r]])

            # remove the left element as long as windowSize - maxOccElem is greater than the chars we are allowed to replace
            while (r - l + 1) - maxOccElem > k:
                freq[s[l]] -= 1
                l += 1

            # Then the windowSize will have consecutive maxOccElem + k elements that we're allowed to replace and will be a valid maxLength value
            maxLength = max(maxLength, (r - l + 1))

        return maxLength
