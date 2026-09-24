# filter() selects items that satisfy a condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(n):
    return n % 2 == 0


result = filter(is_even, numbers)

even_numbers = list(result)

print("Numbers:", numbers)
print("Even numbers:", even_numbers)

#using lambda

odd_numbers = list(filter(lambda n : n % 2 != 0 , numbers))

print("odd numbers :", odd_numbers)
