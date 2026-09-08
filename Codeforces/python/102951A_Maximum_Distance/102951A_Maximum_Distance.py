import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
write = sys.stdout.write


def solve():
    # ------------------ INPUT ------------------
    pass
    n = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    # ------------------ LOGIC ------------------
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist_sq = (xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2
            if dist_sq > res:
                res = dist_sq

    # ------------------ OUTPUT ------------------
    write(str(res) + "\n")


def solution():
    t = int(input())
    for _ in range(t):
        solve()


# No t loop — this is a single-test problem
if __name__ == "__main__":
    solution()
    solve()
