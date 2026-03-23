
numbers = []


numbers = list(map(int, input("Enter numbers separated by space: ").split()))


numbers = sorted(set(numbers))

print("Sorted list without duplicates:", numbers)
