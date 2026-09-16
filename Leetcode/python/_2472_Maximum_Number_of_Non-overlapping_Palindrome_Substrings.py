class Solution:
    # Greedy - Time = O(n * k) - Space = O(1)
    # Iterate over s with i and check if the substring of length k or k + 1 is a palindrome 
    # No need to do the whole expand from center thing because the goal is to find the MAXIMUM non overlapping palindrones of size k, 
    # any palindrome if size > k will already satisfy the size > k condition, so we only look the next k or k + 1 steps, 
    # jump to the right bound of that palindromw with i += k or k + 1 if found, otherwise we jump by 1
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1: return n

        res = 0
        i = 0
        
        while i < n:
            if i + k <= n and s[i:i + k] == s[i:i + k][::-1]:
                res += 1
                i += k
            elif i + k + 1 <= n and s[i:i + k + 1] == s[i:i + k + 1][::-1]:
                res += 1
                i += k + 1
            else:
                i += 1
        
        return res
