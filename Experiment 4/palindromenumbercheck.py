n = int(input("Enter a number: "))
temp = n
rev = 0

while temp:
    rev = rev * 10 + temp % 10
    temp //= 10

print("Palindrome" if n == rev else "Not Palindrome")
