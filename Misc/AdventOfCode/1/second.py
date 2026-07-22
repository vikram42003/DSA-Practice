dial = 50
total = 0

with open("./input.txt") as f:
    for s in f:
        direction = s[0]
        if direction == "R":
            dial = dial + int(s[1:])
            if dial > 100:
                total += 1
                dial %= 100
        else:
            dial = (dial - int(s[1:]))
            if dial < 0:
                total += 1
                dial %= 100
            
        if dial == 0:
            total += 1

print(f"total: {total}")