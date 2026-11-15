import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    inputGrid = [
        list(map(int, input().strip().split())),
        list(map(int, input().strip().split())),
        list(map(int, input().strip().split())),
    ]

    # ------------------ LOGIC ------------------
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    
    for r in range(3):
        for c in range(3):
            # If its odd then it will flip off the light, if its even then it'll be turned
            # back on again
            i = (inputGrid[r][c] & 1)
            
            grid[r][c] ^= i
            
            d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in d:
                if 0 <= r + dr < 3 and 0 <= c + dc < 3:
                    grid[r + dr][c + dc] ^= i
    

    # ------------------ OUTPUT ------------------
    for r in range(3):
        print("".join(str(i) for i in grid[r]))

def solution():
    solve()

if __name__ == "__main__":
    solution()
