from typing import List


class Solution:
    # Backtracking - Time = O(2 ^ n) - Space - O(n)
    # The basic idea is - Whats the biggest palindrome partition we can get from i to j
    # we run a for loop j in range(i, len(s)), in that we check for partition slice from i to j, if its valid append that slice to curr
    # and run dfs(j + 1) to solve for the rest of the array, after that pop the slice we appended, so that we can look at a bigger slice
    # in the next iteration of the loop
    # In the next iteration j will move and our window will get bigger, if the slice is a partiton append it to curr again and look at the 
    # rest of the array, otherwise we dont need to look at this branch any longer
    # BASECASE: We need to find the final array after finding out all combos of the partitions, so add to res only when i >= n 
    
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
