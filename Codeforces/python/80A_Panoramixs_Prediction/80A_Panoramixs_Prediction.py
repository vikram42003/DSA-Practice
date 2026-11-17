import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    a, b = map(int, input().strip().split())

    # ------------------ LOGIC ------------------
    n = -1
    for i in range(a + 1, 51):
        isPrime = True
        for d in range(2, i):
            if i % d == 0:
                isPrime = False
                break
        
        if isPrime == True:
            n = i
            break
        
    # ------------------ OUTPUT ------------------
    print("YES" if n == b else "NO")

def solution():
    solve()

if __name__ == "__main__":
    solution()
