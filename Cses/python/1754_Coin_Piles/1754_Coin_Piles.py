import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
write = sys.stdout.write

# Math trick - Time = O(n) - Space = O(1)
# for both coin piles to go to 0, if we observe, we have two conditions
# - we subtract 2 from one pair 1 form the other, so if the smaller * 2 crosses the larger, then it cant go to 0
#   since we would have some left no matter what
# - we subtract 2 from one pair 1 from the other so the total of a + b gotta be divisible by 3
def solution():
    # ------------------ INPUT ------------------
    n = int(input())
    coins = []
    for _ in range(n):
        a, b = map(int, input().split())
        coins.append((a, b))

    # ------------------ LOGIC ------------------
    res = []
    for a, b in coins:
        if (a + b) % 3 == 0 and max(a, b) <= 2 * min(a, b):
            res.append("YES")
        else:
            res.append("NO")

    # ------------------ OUTPUT ------------------
    write("\n".join(res) + "\n")
    return


if __name__ == "__main__":
    solution()
