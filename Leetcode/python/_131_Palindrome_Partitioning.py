from typing import List


class Solution:
    # Backtracking - Time = O(2 ^ n) - Space - O(n)
    # For s = "aab", the branches of the descision tree will look like this (invalid branches marked by X)
    #                                  "aab"
    #             /                     |                 \
    #          ["a"]                  ["aa"]             ["aab"](X)
    #      /           \                |
    # ["a","a"]      ["a","ab"](X)  ["aa","b"]
    #     |
    # ["a","a","b"]
    def partition(self, s: str) -> List[List[str]]:
        res, curr, n = [], [], len(s)

        def dfs(i):
            if i >= n:
                res.append(curr[:])
                return

            for j in range(i, n):
                # Check for palindrome
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    curr.append(s[i : j + 1])
                    dfs(j + 1)
                    curr.pop()

        dfs(0)
        return res
