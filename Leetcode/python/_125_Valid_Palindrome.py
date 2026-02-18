import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = re.sub("[^a-z0-9]", "", s.lower())
        return newS == newS[::-1]
