import sys

input = sys.stdin.readline
write = sys.stdout.write


friends = int(input().strip())
fingers = sum(map(int, input().strip().split()))

res = 0
for i in range(1, 6):
    if (fingers + i) % (friends + 1) != 1:
        res += 1

print(res)
