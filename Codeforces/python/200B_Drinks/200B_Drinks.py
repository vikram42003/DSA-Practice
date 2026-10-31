import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    # Number of Drinks
    n = int(input())
    # Percentage ratio of Orange Juice in each drink
    juices = list(map(int, input().split()))

    # ------------------ LOGIC ------------------
    res = sum(juices) / (n * 100)

    # ------------------ OUTPUT ------------------
    print(res * 100)

def solution():
    solve()

if __name__ == "__main__":
    solution()
