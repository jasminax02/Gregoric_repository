"""
PowerOfTen
"""
# Provide your solution here
number = -1
while not (0 <= number < 1000):
    number = int(input("Enter a max 3 digit number: "))
    if number < 0:
        print("Number cannot be negative")
    if number > 999:
        print("Number has more than 3 digits")

hundreds_digit = number//100
tens_digit = (number//10) % 10
ones_digit = number % 10
if hundreds_digit > 0 and tens_digit == 0 and ones_digit > 0:
    powersOfTen = str(f"{number} = {hundreds_digit} * 100 + {ones_digit} * 1")
elif hundreds_digit != 0:
    powersOfTen = str(f"{number} = {hundreds_digit} * 100 + {tens_digit} * 10 + {ones_digit} * 1")
elif hundreds_digit == 0 and tens_digit == 0:
    powersOfTen = str(f"{number} = {ones_digit} * 1")
elif hundreds_digit == 0:
    powersOfTen = str(f"{number} = {tens_digit} * 10 + {ones_digit} * 1")
print(powersOfTen)




"""
Cash Box
"""
# Provide your solution here
pay = int(input("To pay: "))
while pay < 0:
    print("Negative payment is invalid")
    pay = int(input("To pay: "))

receive = int(input("Received: "))
while receive < 0:
    print("Negative received amount is invalid.")
    pay = int(input("To pay: "))
    while pay < 0:
        print("Negative payment is invalid")
        pay = int(input("To pay: "))
    receive = int(input("Received: "))

while receive < pay:
    print("You did not pay enough.")
    pay = int(input("To pay: "))
    while pay < 0:
        print("Negative payment is invalid")
        pay = int(input("To pay: "))

    receive = int(input("Received: "))
    while receive < 0:
        print("Negative received amount is invalid.")
        pay = int(input("To pay: "))
        while pay < 0:
            print("Negative payment is invalid")
            pay = int(input("To pay: "))
        receive = int(input("Received: "))

change = receive - pay
print(f"Your change is: {change}")

