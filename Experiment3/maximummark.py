marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
p = sum(marks) / 250 * 100
print("Percentage:", p)

grade = ("O" if p >= 90 else
         "E" if p >= 80 else
         "A" if p >= 70 else
         "C" if p >= 50 else
         "F")
print("Grade:", grade)
