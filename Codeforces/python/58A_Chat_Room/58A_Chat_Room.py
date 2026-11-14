import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    s = input().strip()

    # ------------------ LOGIC ------------------
    ref = "hello"
    i, j = 0, 0
    for i in range(len(s)):
        if j < 5 and s[i] == ref[j]:
            j += 1

    # ------------------ OUTPUT ------------------
    print("YES" if j == 5 else "NO")

def solution():
    solve()

if __name__ == "__main__":
    solution()
