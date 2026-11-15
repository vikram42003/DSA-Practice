import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    y, k, n = map(int, input().strip().split())

    # Find the first divisible value for x + y
    # We know that (x + y) is divisible by k, but we dont know x, so we first
    # do y // k to find the first multiple of k which is smaller than y, but for (x + y)
    # to be divisible by k, they gotta be larger so we do a + 1, so now we have a val of y
    # that is definitely greater than k
    # since its greater than k, we can assume that that value can be split such that it is a combination
    # of both x and y (eg. if we had 18 at this point, and k was 6, and y was 12, then we can just do 
    # 18 - 12 = 6 which will be x)
    first = ((y // k) + 1) * k
    
    # If the smallest valid total exceeds n then return -1
    if first > n:
        print("-1")
        return
    
    res = [i - y for i in range(first, n + 1, k)]
    print(*res)

def solution():
    solve()

if __name__ == "__main__":
    solution()
