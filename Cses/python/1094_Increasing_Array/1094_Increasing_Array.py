import sys
sys.setrecursionlimit(10**7)

def solution():
    input = sys.stdin.readline

    # ------------------ INPUT ------------------
    n = int(input().strip())
    arr = list(map(int, input().split()))

    # ------------------ LOGIC ------------------
    res = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            res += arr[i - 1] - arr[i]
            arr[i] = arr[i - 1]

    # ------------------ OUTPUT ------------------
    print(res)


if __name__ == "__main__":
    solution()
