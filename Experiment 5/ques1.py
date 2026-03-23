
a, b = 0, 1
sum_even = 0

print("Fibonacci series:")
for i in range(20):       
    if a > 1000:
        break
    print(a, end=" ")
    if a % 2 == 0:
        sum_even += a
    a, b = b, a + b

print("\n\nSum of even valued terms:", sum_even)

