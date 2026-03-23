# write a function to find the factorial of a number . 
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


num = int(input("Enter a number: "))
print("Factorial of the number is:", factorial(num))
