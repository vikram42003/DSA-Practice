import sys
sys.setrecursionlimit(10**7)


def solution():
    input = sys.stdin.readline

    # ------------------ INPUT ------------------
    n = int(input())
    nums = list(map(int, input().split()))

    # XOR - Time = O(n) - Space = O(1)
    # There is only one digit missing so summing numbers upto 1 to n and
    # summing all digits in nums and then finding the difference would give
    # us the answer
    # ------------------ LOGIC ------------------
    sumOfDigits = 0
    sumOfNums = 0
    
    for i in range(1, n):
        sumOfDigits += i
        sumOfNums += nums[i - 1]
        
    sumOfDigits += n

    xor = sumOfDigits - sumOfNums

    # ------------------ OUTPUT ------------------
    print(xor)


if __name__ == "__main__":
    solution()
