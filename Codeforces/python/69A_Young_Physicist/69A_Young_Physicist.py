import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    n = int(input().strip())

    # ------------------ LOGIC ------------------
    x, y, z = 0, 0, 0
    for _ in range(n):
        a, b, c = map(int, input().strip().split())
        x += a
        y += b
        z += c

    # ------------------ OUTPUT ------------------
    if x == y == z == 0:
        print("YES")
    else:
        print("NO")

def solution():
    solve()

if __name__ == "__main__":
    solution()
