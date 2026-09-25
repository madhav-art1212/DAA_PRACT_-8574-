def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# Driver Code
num = int(input("Enter a number: "))
print("Factorial =", factorial_iterative(num))
