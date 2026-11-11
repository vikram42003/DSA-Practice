import sys

input = sys.stdin.readline
write = sys.stdout.write

""" String Methods - Time = O(n) - Space = O(n)
We can just split at WUB, filter the null/empty strings, and then join it again with spaces
"""


def solve():
    # ------------------ INPUT ------------------
    str = input().strip()

    # ------------------ LOGIC ------------------
    filteredStr = filter(None, str.split("WUB"))

    # ------------------ OUTPUT ------------------
    print(" ".join(filteredStr))

def solution():
    solve()

if __name__ == "__main__":
    solution()
