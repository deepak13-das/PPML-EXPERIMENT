import math


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


d = b*b - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Two real and distinct roots")
    print("Root 1:", root1)
    print("Root 2:", root2)

elif d == 0:
    root = -b / (2*a)
    print("Two real and equal roots")
    print("Root:", root)

else:
    print("No real roots")
