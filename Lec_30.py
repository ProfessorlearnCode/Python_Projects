# Lecture about Recursion of function method
######################################################
# Recursion is a process of defining a function in terms of itself

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)       # We have called a function in itself
    
print(factorial(3))

# Quiz: Write a program to print the fabonacci sequence

def fabonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)

print(fabonacci(6))