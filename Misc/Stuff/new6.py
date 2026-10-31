# Find the longest substring without repeating characters
str = input("Enter the string: ")

seen = set()

maxmax, curmax = 0, 0
l, r = 0, 0
while r < len(str):
    if str[r] not in seen:
        seen.add(str[r])
        curmax += 1
        maxmax = max(maxmax, curmax)
        r += 1
    else:
        while l < r and str[r] in seen:
            seen.remove(str[l])
            curmax -= 1
            l += 1

print(maxmax)
print(str[l:r + 1])