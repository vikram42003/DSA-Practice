import sys

input = sys.stdin.readline
write = sys.stdout.write

# Sliding Window - Time = O(n log n) - Space = O(n)
# We need to pick student count number of puzzles, so to ensure min variation between max and min, we can sort the items
# and then use two pointers to go through the array to find the global min

def solve():
    # ------------------ INPUT ------------------
    # Student Count and Puzzle Count
    sc, pc = map(int, input().strip().split())
    puzzles = list(map(int, input().strip().split()))

    # ------------------ LOGIC ------------------
    puzzles.sort()
    res = float("inf")
    
    l, r = 0, sc - 1
    while r < pc:
        res = min(res, puzzles[r] - puzzles[l])
        r += 1
        l += 1

    # ------------------ OUTPUT ------------------
    print(res)

def solution():
    solve()

if __name__ == "__main__":
    solution()
