import sys

input = sys.stdin.readline
write = sys.stdout.write

"""
f(n) bubbles index 0 to the end, causing a circular left shift: [1, 2, 3, 4] -> [2, 3, 4, 1].
To end up sorted, our input must do the inverse (circular right shift): [4, 1, 2, 3].
"""

def solve():
    n = int(input().strip())
    print(n, *range(1, n))

# def test():
#     # ------------------ INPUT ------------------
#     n = int(input().strip())
#     perm = [i for i in range(1, n + 1)]

#     # ------------------ LOGIC ------------------
#     def rec(x):
#         if x <= 1:
#             return
#         rec(x - 1)
#         perm[x - 1], perm[x - 2] = perm[x - 2], perm[x - 1]
#     rec(n)

#     # ------------------ OUTPUT ------------------
#     print(" ".join(str(p) for p in perm))

def solution():
    solve()

if __name__ == "__main__":
    solution()
