import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    print(*sorted(map(int, input().strip().split("+"))), sep="+")
    

def solution():
    solve()

if __name__ == "__main__":
    solution()
