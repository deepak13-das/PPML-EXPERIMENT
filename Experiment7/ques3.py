# wap to create a string which contain a paragraph. now find 1.count How many word it contains .2.how many palindrome exist .3.print each word in reverse order .
# create a string containing a paragraph
para = input("Enter a paragraph: ")

# split paragraph into words
words = para.split()

# 1. count number of words
word_count = len(words)
print("Total number of words:", word_count)

# 2. count palindromes
pal_count = 0
for word in words:
    w = word.lower()
    if w == w[::-1]:
        pal_count = pal_count + 1

print("Number of palindrome words:", pal_count)

# 3. print each word in reverse order
print("Each word in reverse order:")
for word in words:
    print(word[::-1], end=" ")
 