import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    n = int(input())

    # ------------------ LOGIC ------------------
    maxmax, curmax = 0, 0
    for _ in range(n):
        exiting, entering = map(int, input().split())
        curmax -= exiting
        curmax += entering

        maxmax = max(maxmax, curmax)
        
    # ------------------ OUTPUT ------------------
    print(maxmax)

def solution():
    solve()

if __name__ == "__main__":
    solution()
