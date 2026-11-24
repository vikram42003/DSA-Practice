import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    m = int(input().strip())
    queries = list(map(int, input().strip().split()))

    # ------------------ LOGIC ------------------
    posMap = { num: idx for idx, num in enumerate(nums) }
    vasya, petya = 0, 0
    for q in queries:
        idx = posMap[q]
        vasya += idx + 1
        petya += n - idx

    # ------------------ OUTPUT ------------------
    print(f"{vasya} {petya}")

def solution():
    solve()

if __name__ == "__main__":
    solution()
