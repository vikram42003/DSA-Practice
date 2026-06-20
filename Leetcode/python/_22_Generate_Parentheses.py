from typing import List


class Solution:
    # Backtrack - Time = O(2^2n) = O(4^n) - Space = O(n) or O(n n^4) (if we include res array)
    # The core idea is that we start from an empty string and at each step we have two choices to make
    # - If the opening parenthesis are less than n, we can just add them, adding opening parenthesis' 
    #   will never make it invalid
    # - If the closing parenthesis are less than opening, only then can we add them, cause if we add 
    #   more closing than opening then its immediately invalid
    # Base case will be if opening == closing == n, then we have reached a valid string of required length
    # so add that to res and return res at the end
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # o - open parenthesis count
        # c - close parenthesis count
        # p - the current parenthesis string we're building
        def rec(o, c, p):
            # If open and close and n count are the same that means we've build
            # a valid parenthesis string of size n
            if o == c == n:
                res.append(p)
                return

            # If opening parenthesis are less than n we can keep adding them
            if o < n:
                rec(o + 1, c, p + "(")

            # If closing parenthesis are less than open, only then can we add them
            if c < o:
                rec(o, c + 1, p + ")")

        rec(0, 0, "")
        return res
