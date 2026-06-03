arr = [1,2,4,6,8,9,10]

l, r = 0, len(arr) - 1

while l < r:
    m = l + (r - l) // 2
    if arr[m] >= 6:
        r = m
    else:
        l = m + 1

print(arr[l])