import sys

input = sys.stdin.readline
write = sys.stdout.write

# Greedy Simulation Intuition:
# Always give the next apple to whoever currently has less weight. Because apples
# only weigh 100 or 200, the difference |t - o| can never exceed 200.
# - If |t - o| == 0: Already split evenly.
# - If |t - o| == 100: Total weight is an odd multiple of 100 -> impossible.
# - If |t - o| == 200: Total weight is even, so we must have an even count of 100s.
#   Having at least one 100 means we actually have >= 2, allowing us to swap
#   two 100s against one 200 to close the 200g gap.

def solve():
    # ------------------ INPUT ------------------
    n = int(input().strip())
    apples = list(map(int, input().strip().split()))

    # ------------------ LOGIC ------------------
    t, o = 0, 0
    extra_100s_for_balancing = 0
    for a in apples:
        if a == 100:
            extra_100s_for_balancing += 1
            
        if t < o:
            t += a
        else:
            o += a
    
    # ------------------ OUTPUT ------------------
    if abs(t - o) == 0 or (abs(t - o) == 200 and extra_100s_for_balancing > 0):
        print("YES")
    else:
        print("NO")
        
# Counting / Parity Math:
# Divide all weights by 100 so apples are just 1s and 2s.
# 1. Total sum (c100 + 2*c200) must be even -> c100 must be even.
# 2. Each person needs half the sum: (c100 // 2) + c200.
#    - If c200 is even, split the 2s evenly and split the 1s evenly.
#    - If c200 is odd, one person gets an extra 2 (+200g), so the other needs
#      two 1s (+200g) to match it -> requires c100 >= 2.

# def solve():
#     n = int(input().strip())
#     apples = list(map(int, input().strip().split()))
#     c100 = apples.count(100)
#     c200 = apples.count(200)

#     if c100 % 2 == 0 and (c200 % 2 == 0 or c100 >= 2):
#         print("YES")
#     else:
#         print("NO")

def solution():
    solve()

if __name__ == "__main__":
    solution()
