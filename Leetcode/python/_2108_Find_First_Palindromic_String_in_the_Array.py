from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i, j = 0, len(word) - 1
            while i < j and word[i] == word[j]:
                i += 1
                j -= 1

            if i >= j:
                return word

        return ""

    # Oneline
    # We're calling next for that iterator and passing "" as the default value
    def firstPalindrome(self, words: List[str]) -> str:
        return next((word for word in words if word == word[::-1]), "")