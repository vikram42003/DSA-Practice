import sys
sys.setrecursionlimit(10**7)

def solution():
    input = sys.stdin.readline

    # ------------------ INPUT ------------------
    n = int(input().strip())

    # ------------------ LOGIC ------------------
    if n == 1:
        print("1")
        return
    elif n < 4:
        print("NO SOLUTION")
        return
    
    evens = range(2, n + 1, 2)
    odds = range(1, n + 1, 2)

    # ------------------ OUTPUT ------------------
    print(" ".join(map(str, evens)) + " " + " ".join(map(str, odds)))
    return


if __name__ == "__main__":
    solution()
