import sys
from collections import Counter

input = sys.stdin.readline
write = sys.stdout.write


def solve():
    a = input().strip()
    b = input().strip()
    pile = input().strip()

    ab = a + b

    if len(ab) != len(pile) or Counter(ab) != Counter(pile):
        print("NO")
    else:
        print("YES")


def solution():
    solve()


if __name__ == "__main__":
    solution()
