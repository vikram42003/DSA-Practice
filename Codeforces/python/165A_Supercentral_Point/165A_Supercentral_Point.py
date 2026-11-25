import sys

input = sys.stdin.readline
write = sys.stdout.write


n = int(input().strip())
points = set()
maxX, minX, maxY, minY = -1, -1, -1, -1
for _ in range(n):
    x, y = map(int, input().strip().split())
    maxX, minX, maxY, minY = max(maxX, x), min(minX, x), max(maxY, y), min(minY, y)
    points.add((x, y))

res = 0
for x, y in points:
    top, bottom, left, right = False, False, False, False
    for i in range(x + 1, maxX + 1):
        if (i, y) in points:
            right = True
            break
    for i in range(x - 1, minX - 1, -1):
        if (i, y) in points:
            left = True
            break
    for i in range(y + 1, maxY + 1):
        if (x, i) in points:
            top = True
            break
    for i in range(y - 1, minY - 1, -1):
        if (x, i) in points:
            bottom = True
            break
    if top and bottom and left and right:
        res += 1

print(res)
