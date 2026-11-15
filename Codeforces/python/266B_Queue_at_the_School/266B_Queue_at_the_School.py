import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    n, t = map(int, input().strip().split())
    arr = list(input().strip())

    # ------------------ LOGIC ------------------
    for _ in range(t):
        newArr = [arr[0]]
        for i in range(1, n):
            if arr[i - 1] == "B" and arr[i] == "G":
                newArr[-1] = "G"
                newArr.append("B")
            else:
                newArr.append(arr[i])
        arr = newArr

    # ------------------ OUTPUT ------------------
    print("".join(arr))

def solution():
    solve()

if __name__ == "__main__":
    solution()
