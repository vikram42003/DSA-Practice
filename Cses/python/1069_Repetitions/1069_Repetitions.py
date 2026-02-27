from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

def solution():
    input = sys.stdin.readline

    # ------------------ INPUT ------------------
    seq = input().strip()

    # ------------------ LOGIC ------------------
    cur, res = 1, 1
    for i in range(1, len(seq)):
        if seq[i - 1] == seq[i]:
            cur += 1
            res = max(res, cur)
        else:
            cur = 1

    # ------------------ OUTPUT ------------------
    print(res)


if __name__ == "__main__":
    solution()
