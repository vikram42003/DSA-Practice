import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    # ------------------ LOGIC ------------------
    minH, maxH, minIdx, maxIdx = float("inf"), float("-inf"), -1, -1
    for i in range(n):
        if arr[i] > maxH:
            maxH = arr[i]
            maxIdx = i
        
        if arr[i] <= minH:
            minH = arr[i]
            minIdx = i

    res = maxIdx + (n - minIdx - 1)
    # Deduct an extra 1 if min and max would cross each other
    if minIdx < maxIdx:
        res -= 1
    # ------------------ OUTPUT ------------------
    print(res)

def solution():
    solve()

if __name__ == "__main__":
    solution()
