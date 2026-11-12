import sys

input = sys.stdin.readline
write = sys.stdout.write

""" Math - Time = O(1) - Space = O(1)
Split into two halves using odd_count = (n + 1) // 2:
- First half (k <= odd_count): 2 * k - 1
- Second half (k > odd_count): 2 * (k - odd_count)

Example - 7 3 (odd_count = 4)
k                      -      1  2  3  4 | 5  6  7
Adjusted k             -      1  2  3  4 | 1  2  3
Numbers in the pattern -      1  3  5  7 | 2  4  6
"""


def solve():
    # ------------------ INPUT ------------------
    n, k = map(int, input().split())

    # ------------------ LOGIC ------------------
    odd_count = (n + 1) // 2

    if k <= odd_count:
        res = 2 * k - 1
    else:
        k -= odd_count
        res = 2 * k

    # ------------------ OUTPUT ------------------
    print(res)


def solution():
    solve()


if __name__ == "__main__":
    solution()
