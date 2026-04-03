import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
write = sys.stdout.write

# Math Trick - Time = O(log5n) - Space = O(1)
# The number of zeros can be found out by adding up all the factors of 5 in the numbers from 1 to n, 
# but there are nuances like if n = 251 then there will be 25 as a factor, which is 5 * 5
# So a generalized formula is  `n / i` where i is 5 and gets multiplied by 5 each time until its > n
def solution():
    # ------------------ INPUT ------------------
    n = int(input())

    # ------------------ LOGIC ------------------
    i = 5
    total = 0
    while i <= n:
        total += n // i
        i *= 5

    # ------------------ OUTPUT ------------------
    write(str(total) + "\n")
    return


if __name__ == "__main__":
    solution()
