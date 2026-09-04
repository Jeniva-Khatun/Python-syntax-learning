# 3. Search for a character in a string using for...else

text = input("Enter a string: ")
target = input("Enter a character to search: ")

for char in text:
    if char == target:
        print("Found")
        break
else:
    print("Not Found")
