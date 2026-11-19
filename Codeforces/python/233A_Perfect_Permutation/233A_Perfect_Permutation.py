import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    n = int(input().strip())

    if (n & 1) == 1:
        print("-1")
        return

    res = []
    for i in range(2, n + 1, 2):
        res.append(i)
        res.append(i - 1)
    
    print(*res)

def solution():
    solve()

if __name__ == "__main__":
    solution()
