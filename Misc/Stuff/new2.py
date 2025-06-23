# Program 1
bill = int(input("Enter bill amt - "))
if bill >= 1000:
    print("Final bill is ", (bill - (bill * 0.1)))
else:
    print("Final bill is ", bill)
    
# Program 2
sub1 = int(input("Subject 1 - "))
sub2 = int(input("Subject 2 - "))
sub3 = int(input("Subject 3 - "))

if sub1 > 75 and sub2 > 75 and sub3 > 75:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

# Program 3
itemA = True
itemB = True

if itemA and itemB:
    print("Valid for combo offer")
else:
    print("Not valid for combo offer")
    
# Program 5
city1 = 35
city2 = 30

city1 = city1 ^ city2
city2 = city1 ^ city2
city1 = city1 ^ city2

print("city1 temp is", city1)
print("city2 temp is", city2)