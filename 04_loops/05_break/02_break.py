# 2. Search for a given number in a list and stop when found
#
#
numbers = [10, 20, 30, 40, 50]

target = int(input("Enter number to search: "))

for num in numbers:
    if num == target:
        print("Number found!")
        break
else:
    print("Number not found.")
