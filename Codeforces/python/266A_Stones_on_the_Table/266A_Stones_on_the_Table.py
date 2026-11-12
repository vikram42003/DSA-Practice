import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    n = int(input())

    # ------------------ LOGIC ------------------
    res = []
    for s in input().strip():
        if len(res) == 0 or res[-1] != s:
            res.append(s)

    # ------------------ OUTPUT ------------------
    print(n - len(res))

def solution():
    solve()

if __name__ == "__main__":
    solution()
