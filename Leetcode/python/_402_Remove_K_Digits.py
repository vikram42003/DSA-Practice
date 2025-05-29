class Solution:
    # Monotonic Stack Approach - Time O(n) - Space = O(n)

    # The intuition is -
    # We need to remove k digits right, so if k = 3 and num is 54321 - then it makes sense to remove the first 3 digits
    # so num will be 45
    # But if k = 3 and num = 12345, then we need to remove the last 3 digits

    # So the pattern is keep num in an ascending order, if a digit breaks that order then remove it
    # But if after that previous process, we are left with any more digits we can remove then remove them from the back

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        # Mantain an ascending monotonic stack
        stack = []

        # Iterate over all digits in num
        for n in num:
            # While we have k digits to remove
            # And stack has some digits for us to remove
            # And the current digit is less than stack top, breaking the asc order
            # Then remove the stack top and decrement k
            # Also we can just compare n and stack[-1] directly since theyre both strings
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            # Append the current digit to stack
            stack.append(n)

        # If we are left with some more digits we can remove then just remove k digits from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Store the final ans in ans and remove any leading 0s
        ans = ""
        for s in stack:
            if not ans and s == "0":
                continue
            ans += s

        # return "0" if ans is empty string
        return ans if ans else "0"
