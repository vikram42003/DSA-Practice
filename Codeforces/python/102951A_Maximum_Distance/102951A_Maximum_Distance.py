import sys

input = sys.stdin.readline
write = sys.stdout.write


def solve():
    # ------------------ INPUT ------------------
    n = int(input().strip())
    xs = list(map(int, input().strip().split()))
    ys = list(map(int, input().strip().split()))

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
    solve()


if __name__ == "__main__":
    solution()
