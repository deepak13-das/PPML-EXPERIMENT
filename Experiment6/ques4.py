# / wap to input a sentence .store each word as a element in to a list 1. now display the element of list along with its index (using enumerate()). create another list LIST2 having elements as a series of numbers. now use zip() to combine the element of both list to create a 3rd list3 and then display it.

sentence = input("Enter a sentence: ")


list1 = sentence.split()


print("\nElements of LIST1 with index:")
for index, word in enumerate(list1):
    print(index, ":", word)


list2 = list(range(1, len(list1) + 1))


list3 = list(zip(list1, list2))


print("\nCombined LIST3 using zip():")
print(list3)
 