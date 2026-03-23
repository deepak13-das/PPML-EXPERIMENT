
P = float(input("Enter the Principal Amount: "))
R = float(input("Enter the Rate of Interest: "))
T = float(input("Enter the Time in Years: "))

simple_interest = (P * R * T) / 100

compound_interest = P * (1 + R/100) *T - P

print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
