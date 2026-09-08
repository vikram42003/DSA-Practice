class Solution:
    # Freq maps - Time = O(n) - Space = O(1)
    # Count the frequency of chars in strings s1 and s2 in freq_s1 and freq_s2
    # Then Count the frequency of chars in s2 within a sliding window, return True on match
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1, freq_s2 = [0] * 26, [0] * 26
        n, m = len(s1), len(s2)

        for s in s1:
            freq_s1[ord(s) - 97] += 1
        
        l, r = 0, 0
        while r < m:
            freq_s2[ord(s2[r]) - 97] += 1
            
            if r - l >= n:
                freq_s2[ord(s2[l]) - 97] -= 1
                l += 1
            
            if all(freq_s1[i] == freq_s2[i] for i in range(26)):
                return True
            
            r += 1
        
        return False
