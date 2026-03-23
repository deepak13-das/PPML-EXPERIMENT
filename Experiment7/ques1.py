# wap to create a list containg natunal number from m to n where m and n given input.(CREATE USING FOR LOOP.)find sum, average largest and smallest in the list. create another list which contains all the members of 1 st list expect number divisible by 3 .
# input m and n
m = int(input("Enter starting number (m): "))
n = int(input("Enter ending number (n): "))

# create list from m to n
lst = []
for i in range(m, n + 1):
    lst.append(i)

print("List:", lst)

# find sum
total = 0
for i in lst:
    total = total + i

# find average
avg = total / len(lst)

# find largest and smallest
largest = lst[0]
smallest = lst[0]

for i in lst:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Sum =", total)
print("Average =", avg)
print("Largest =", largest)
print("Smallest =", smallest)

# create new list excluding numbers divisible by 3 (using nested loop)
new_list = []
for i in lst:
    flag = 1
    for j in range(3, 4):     # nested loop
        if i % j == 0:
            flag = 0
    if flag == 1:
        new_list.append(i)

print("List excluding numbers divisible by 3:", new_list)
 