import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
write = sys.stdout.write


# Fast Exponentiation - Time = O(log n) - Space = O(1)
# take res = 1, a is the number, b is the power
# res is the final res, a is the next batch of pows we wanna do at once
# if b is odd, we do res = (res * a) % mod, decrasing the number of times we need to pow (b) by 1
# if b is even or after b is now even we do a = a * a % mod, effectively halfing the number of times we need to pow
def solution():
    # ------------------ INPUT ------------------
    b = int(input())

    # ------------------ LOGIC ------------------
    res = 1
    a = 2
    mod = int(1e9 + 7)

    while b > 0:
        if b & 1:
            res = (res * a) % mod
        a = a * a % mod
        b >>= 1

    # ------------------ OUTPUT ------------------
    write(str(res) + "\n")
    return


if __name__ == "__main__":
    solution()
