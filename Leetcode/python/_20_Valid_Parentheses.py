class Solution:
    # Stack - Time = O(n) - Space = O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            condition = stack and (
                (stack[-1] == "(" and c == ")")
                or (stack[-1] == "[" and c == "]")
                or (stack[-1] == "{" and c == "}")
            )
            if condition:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
