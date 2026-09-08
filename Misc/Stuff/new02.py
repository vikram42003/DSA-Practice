def isEven(num: int) -> bool:
    return (num & 1) == 0

print(isEven(10))
print(isEven(7))
print(isEven(5))

def canVote(age: int) -> bool:
    return age >= 18

print(f"Can a person with the age 16 vote? {canVote(16)}")
print(f"Can a person with the age 20 vote? {canVote(20)}")