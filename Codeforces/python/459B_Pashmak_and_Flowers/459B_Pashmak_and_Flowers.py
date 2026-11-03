import sys

input = sys.stdin.readline
write = sys.stdout.write

""" Min/Max + Combinations - Time = O(n) - Space = O(n)
Find the max diff, and the occurances of maxVal dna minVal and their product, and return both
Edgecase
- If both min and max are the same vals, then the combinations will be n(n - 1) / 2
"""


def solve():
    # ------------------ INPUT ------------------
    n = int(input())
    flowers = list(map(int, input().split()))

    # ------------------ LOGIC ------------------
    maxVal, minVal, counter = float("-inf"), float("inf"), {}
    for f in flowers:
        maxVal, minVal = max(maxVal, f), min(minVal, f)
        counter[f] = counter.get(f, 0) + 1
    
    # Edgecase - If both are the same numbers use the combinations equation
    if minVal == maxVal:
        print(f"0 {(n * (n - 1)) // 2}")
        return

    maxDiff = maxVal - minVal
    combinations = counter[maxVal] * counter[minVal]

    # ------------------ OUTPUT ------------------
    print(f"{maxDiff} {combinations}")


def solution():
    solve()


if __name__ == "__main__":
    solution()
