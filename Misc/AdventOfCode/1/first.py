dial = 50
total = 0

with open("./input.txt") as f:
    for s in f:
        direction = s[0]
        if direction == "R":
            dial = (dial + int(s[1:])) % 100
        else:
            dial = (dial - int(s[1:])) % 100
            
        if dial == 0:
            total += 1

print(f"total: {total}")

# with open("./input.txt") as f:
#     for line in f:
#         print("Dial: ", dial)
#         s = input("Input: ")
        
#         if len(s) < 2 or len(s) > 3:
#             print("Incorrect input")
#             continue
            
#         try:
#             direction = s[0]
#             if direction == "R" or direction == "r":
#                 dial = (dial + int(s[1:3])) % 100
#             elif direction == "L" or direction == "l":
#                 if dial == 0:
#                     total += 1
#                 dial = (dial - int(s[1:3])) % 100
#             else:
#                 print("Incorrect input")
#                 continue
#         except Exception as e:
#             print(e)
#             print("Incorrect input")