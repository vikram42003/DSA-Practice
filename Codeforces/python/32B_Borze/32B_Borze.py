import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    str = input().strip()

    # ------------------ LOGIC ------------------
    res = []
    n = len(str)
    i = 0
    while i < n:
        if str[i] == ".":
            res.append("0")
            i += 1
        elif str[i] == "-" and str[i + 1] == ".":
            res.append("1")
            i += 2
        else:
            res.append("2")
            i += 2

    # ------------------ OUTPUT ------------------
    print("".join(res))

def solution():
    solve()

if __name__ == "__main__":
    solution()
