# reduce() combines all items into a single value

from functools import reduce


numbers = [1, 2, 3, 4, 5]


def add(a, b):
    return a + b


result = reduce(add, numbers)

print("Numbers:", numbers)
print("Sum:", result)


# Using lambda
product = reduce(
    lambda a, b: a * b,
    numbers
)

print("Product:", product)
