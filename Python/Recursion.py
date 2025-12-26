print("Recursion...!!!")

def factiorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factiorial(n-1)

num = int(input("Enter a number to find factorial: "))
result = factiorial(num)
print(f"The factiorial of {num} is {result}")

def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    else:
        fib_seq = fibonacci(n-1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
num = int(input("Enter the number of terms for Fibonacci series: "))
fib_series = fibonacci(num)
print(f"The first {num} terms of the Fibonacci series are: {fib_series}")


