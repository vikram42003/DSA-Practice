from typing import List


class Solution:
    # Backtracking - Time = (4 ^ n) - Space = O(n)
    # Store the letters in an array like ["abc", "def", ...] and convert digits (eg. "23" to 01) so that we can correspond it with the array easier
    # Run a recursive dfs, at each level, pick each digit in a loop and recurse to next level, until we reach 
    # base case i >= n, then append to res with "".join(curr) and then pop out the digit after using it
    
    # Cleaner Version
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        res, n = [], len(digits)

        def dfs(i, curr):
            if i >= n:
                res.append(curr[:])
                return

            for l in letters[int(digits[i]) - 2]:
                dfs(i + 1, curr + l)

        dfs(0, "")
        return res
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        res, curr, n = [], [], len(digits)

        def dfs(i):
            if i >= n:
                res.append("".join(curr))
                return
            
            # corresponding element of letters for digit[i]
            d = int(digits[i]) - 2
            for j in range(len(letters[d])):
                curr.append(letters[d][j])
                dfs(i + 1)
                curr.pop()

        dfs(0)

        return res