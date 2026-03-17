import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
write = sys.stdout.write


# First check if n(n+1)/2 is even, to check if the total sum can even be divided into two equal sets, then
# Build one subset greedily from largest numbers so you hit exactly half of total sum.


def solution():
    # ------------------ INPUT ------------------
    n = int(input().strip())

    # ------------------ LOGIC ------------------
    res = []

    total = n * (n + 1) // 2
    if total % 2:
        write("NO\n")
        return

    target = total // 2
    set1, set2 = [], []
    
    for i in range(n, 0, -1):
        if i <= target:
            set1.append(i)
            target -= i
        else:
            set2.append(i)

    res = [
        "YES",
        str(len(set1)),
        " ".join(map(str, set1)),
        str(len(set2)),
        " ".join(map(str, set2)),
    ]

    # ------------------ OUTPUT ------------------
    write("\n".join(res) + "\n")
    return


if __name__ == "__main__":
    solution()
