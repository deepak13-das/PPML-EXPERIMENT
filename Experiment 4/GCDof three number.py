
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

while b != 0:
    a, b = b, a % b
    
b = c
while b != 0:
    a, b = b, a % b

print(f"GCD of the three numbers is {a}")
