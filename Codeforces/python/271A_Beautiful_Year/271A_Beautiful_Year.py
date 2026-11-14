import sys

input = sys.stdin.readline
write = sys.stdout.write


def solve():
    year = int(input().strip())

    while True:
        year += 1
        s = str(year)
        if len(set(s)) == len(s):
            print(year)
            break


def solution():
    solve()


if __name__ == "__main__":
    solution()
