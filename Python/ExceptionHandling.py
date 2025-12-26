print("Exception Handling in Python...!!!")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed and i am Always executed.")
print("Done...!!!")



# custom Error

a = int(input("Enter a Value between 1 to 10: "))

if a<1 or a>10:
    raise ValueError("Value is Out of range please enter between 1 to 10")


