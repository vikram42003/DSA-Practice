for i in range(1, 51):
    text = ""
    if i % 3 == 0:
        text += "Fizz"
    if i % 5 == 0:
        text += "Buzz"
        
    print(f"{i}: {text}")




# marks = int(input("Enter the marks: "))

# if marks >= 90:
#     print("A")
# elif marks >= 80:
#     print("B")
# elif marks >= 70:
#     print("C")
# elif marks >= 60:
#     print("D")
# else:
#     print("F")