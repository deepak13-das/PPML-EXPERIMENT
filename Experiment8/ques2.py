#  write a function to check whether a number is even or add. 
def check_even_odd(n):
    if n % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")


num = int(input("Enter a number: "))
check_even_odd(num)
