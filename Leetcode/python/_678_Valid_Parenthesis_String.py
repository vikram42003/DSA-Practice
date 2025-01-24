class Solution:
    # Greedy - Time = O(n) - Space = O(1)
    def checkValidString(self, s: str) -> bool:
        # maxPar and minPar track the maximum and minimum number of open '('
        # we can have up to this point.
        #
        # '(' and ')' are deterministic: they increase or decrease both bounds equally.
        # '*' is flexible:
        #   - If used as '(', it increases maxPar
        #   - If used as ')', it decreases minPar
        #   - If used as empty, it leaves the count unchanged
        #
        # Therefore, [minPar, maxPar] represents the range of possible open
        # parentheses counts at the current position.
        maxPar, minPar = 0, 0

        for i in s:
            if i == "(":
                maxPar += 1
                minPar += 1
            elif i == ")":
                maxPar -= 1
                minPar -= 1
            else:  # '*'
                maxPar += 1
                minPar -= 1

            # If even in the most optimistic case (using all '*' as '(')
            # we have more ')' than we can match, the string is invalid.
            if maxPar < 0:
                return False

            # minPar can go negative if we aggressively use '*' as ')'.
            # We clamp it to 0 because we can instead treat those '*' as empty.
            if minPar < 0:
                minPar = 0

        # If the minimum possible number of open '(' at the end is 0,
        # then there exists a valid substitution.
        return minPar == 0
