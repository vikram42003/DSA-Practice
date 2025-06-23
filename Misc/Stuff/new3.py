# Find greatest of 4 numbers using if
a = 10
b = 25
c = 15
d = 20

if a >= b and a >= c and a >= d:
    greatest = a
elif b >= a and b >= c and b >= d:
    greatest = b
elif c >= a and c >= b and c >= d:
    greatest = c
else:
    greatest = d

print("The greatest number is:", greatest)

# Outfit based on weather
weather = input("Enter the current weather (sunny, rainy, snowy, windy, cloudy): ")

if weather == "sunny":
    print("Wear a t-shirt, sunglasses, and sunscreen.")
elif weather == "rainy":
    print("Bring an umbrella and wear a waterproof jacket.")
elif weather == "snowy":
    print("Wear a heavy coat, gloves, and boots.")
elif weather == "windy":
    print("Wear a windbreaker or a light jacket.")
elif weather == "cloudy":
    print("Wear something light but carry a jacket just in case.")
else:
    print("Invalid weather condition. Please try again.")

# ATM with loop
balance = 10000

print("Welcome to the ATM.")
print("Your starting balance is ", balance)

while balance > 0:
        amount = int(input("Enter amount to withdraw (0 to exit): "))

        if amount == 0:
            print("Thank you for using the ATM. Goodbye!")
            break
        elif amount < 0:
            print("Invalid amount. Please enter a positive value.")
        elif amount > balance:
            print("Insufficient balance. You have ", balance)
        else:
            balance -= amount
            print("Withdrawal successful. Remaining balance: ", balance)

if balance == 0:
    print("Your account balance is 0. Exiting...")

# Password check with 3 attempts
correct_password = "12345"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    entered_password = input("Enter your password: ")

    if entered_password == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts += 1
        print("Incorrect password. Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Account locked due to 3 failed attempts.")