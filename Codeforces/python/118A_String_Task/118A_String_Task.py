import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    str = input().strip().lower()

    # ------------------ LOGIC ------------------
    res = []
    for s in str:
        if s not in ["a", "o", "y", "e", "u", "i"]:
            res.append(".")
            res.append(s)

    # ------------------ OUTPUT ------------------
    write("".join(res))

def solution():
    solve()

if __name__ == "__main__":
    solution()
