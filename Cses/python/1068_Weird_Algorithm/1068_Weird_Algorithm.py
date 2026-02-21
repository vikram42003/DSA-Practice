import sys
sys.setrecursionlimit(10**7)

def solution():
    input = sys.stdin.readline

    # ------------------ INPUT ------------------
    n = int(input().strip())

    # ------------------ LOGIC ------------------
    res = "" + str(n)
    
    while n != 1:
        if (n & 1) == 0:
            n //= 2
            res += " " + str(n)
        else:
            n = (n * 3) + 1
            res += " " + str(n)

    # ------------------ OUTPUT ------------------
    print(res)


if __name__ == "__main__":
    solution()
