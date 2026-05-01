from typing import List


class Solution:
    # Python is fucking stupid we cant really do a isdigit() or isnumeric() to chekc
    # if a number like "-11" is a number, so checking for the operators instead
    # Do be careful about this
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                a, b = stack.pop(), stack.pop()
                res = 0
                if t == "+":
                    res = a + b
                elif t == "-":
                    res = b - a
                elif t == "*":
                    res = a * b
                else:
                    res = int(b / a)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]
