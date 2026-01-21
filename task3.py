##problem statement-1
import math


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")

##problem statement-2
num1 = int(input("Enter a number : "))

sqrt=math.sqrt(num1)
log=math.log(num1)
#angle=math.radians(num1)
sine =math.sin(num1)

print(f"Square root of {num1}: {sqrt}")
print(f"Natural logarithm of {num1}: {log}")
print(f"Sine of {num1}: {sine}")