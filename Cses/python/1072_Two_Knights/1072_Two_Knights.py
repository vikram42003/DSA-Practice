import sys

sys.setrecursionlimit(10**7)


# Math - Time = O(n^2) - Space = O(1)
# Dont try DP, Its a Math one
# for any k, number of ways to place 2 knights without attacking each other = number of ways to place 2 knights - number of ways to place knights so that they attack each other
# number of ways to place 2 knights = kC2 = ((k) * (k - 1)) / 2 (Math Combinations)
# number of ways to place knights so that they attack each other - Two knights attack each other only when they occupy opposite corners of a 2×3 (or 3×2) rectangle, so you just count how many such rectangles fit in the board and multiply by the two attacking placements each rectangle allows.
# So (k - 1)(k - 2) horizontal positions + (k- 2)(k - 1) vertical positions
# = 2(k - 1)(k - 2) * 2 (One for each knight, we have 2 knights)
# = 4(k - 1)(k - 2)


def solution():
    input = sys.stdin.readline
    output = sys.stdout.write

    # ------------------ INPUT ------------------
    n = int(input().strip())

    # ------------------ LOGIC ------------------
    for i in range(1, n + 1):
        board = i * i
        total = (board * (board - 1)) // 2
        attack = 4 * (i - 1) * (i - 2)
        # ------------------ OUTPUT ------------------
        print(total - attack)

    return


if __name__ == "__main__":
    solution()
