print("Functions.py file")

def greet(name):
    return (f"Hello GA, {name}!")

print(greet("Arun"))

def greet(name):
    print (f"Hello GM, {name}!")

greet("Arun")


def add(a,b): # a and b are parameters
    return a + b

i = int(input("Enter first number: "))
j = int(input("Enter second number: "))

print(f"The Sum of {i} and {j} is {add(i,j)}") # i am passing i and j as arguments

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number to find factorial: "))
print(f"The factorial of {num} is {factorial(num)}")


def fibonacci(n):
    pass



