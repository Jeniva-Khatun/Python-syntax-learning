# 1. Search for a number using for...else

numbers = [10, 20, 30, 40, 50]

target = int(input("Enter a number to search: "))

for num in numbers:
    if num == target:
        print("Found")
        break
else:
    print("Not Found")
