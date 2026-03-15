import sys
sys.setrecursionlimit(10**7)

def solution():
    input = sys.stdin.readline

    # ------------------ INPUT ------------------
    n = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # ------------------ LOGIC ------------------
    for x, y in arr:
        layer = max(x, y)
        base = layer ** 2
        
        if (layer & 1) == 0:
            base -= layer - x
            base -= y - 1
        else:
            base -= layer - y
            base -= x - 1
        
        print(base)

    # ------------------ OUTPUT ------------------
    return


if __name__ == "__main__":
    solution()
