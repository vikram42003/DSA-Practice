import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    num = input().strip()
    n = len(num)

    # ------------------ LOGIC ------------------
    res = "YES"
    i = 0
    while i < n:
        if i + 2 < n and num[i:i + 3] == "144":
            i += 3
        elif i + 1 < n and num[i:i + 2] == "14":
            i += 2
        elif num[i] == "1":
            i += 1
        else:
            res = "NO"
            break

    # ------------------ OUTPUT ------------------
    print(res)

def solution():
    solve()

if __name__ == "__main__":
    solution()
