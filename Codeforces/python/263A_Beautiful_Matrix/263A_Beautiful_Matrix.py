import sys

input = sys.stdin.readline
write = sys.stdout.write

""" 2D Traversal - Time = O(1) - Space = O(1)
Well we know that the input will be a 5x5 matrix of numbers so we can just directly
look for the 1 and then check its offset from the center on x and y axis and return that sum
"""


def solve():
    # ------------------ INPUT ------------------
    # ------------------ LOGIC ------------------
    for r in range(5):
        row = list(map(int, input().split()))
        for c in range(5):
            if row[c] == 1:
                print(abs(2 - r) + abs(2 - c))

    # ------------------ OUTPUT ------------------
    return -1


def solution():
    solve()


if __name__ == "__main__":
    solution()
