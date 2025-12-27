print("If-Else Statements in Python")
a = 10
b = 20
if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{b} is greater than {a}")


# Nested If-Else
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("You entered zero")
    else:
        print("You entered a positive number")
else:
    print("You entered a negative number")


# Check even or odd
if num % 2 ==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# practices

import time

time_now = time.localtime()
hour = time_now.tm_hour
if hour < 12:
    print("Good Morning!")
elif 12 <= hour < 18:
    print("Good Afternoon!")                                            
else:
    print("Good Evening!")  


#match -case (Python 3.10+)
day = int(input("Enter day number (0-6): "))
match day:
    case 0:
        print("Sunday")
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case _:
        print("Invalid day number")
    
# Nested match-case
month = int(input("Enter month number (1-12): ")) 
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case 2:
        year = int(input("Enter year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("29 days")
        else:
            print("28 days")
    case _:
        print("Invalid month number")


# short hand if-else
