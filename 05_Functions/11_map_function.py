# map() applies a function to every item

numbers = [1, 2, 3, 4, 5]

def square(n):
    return n * n


result = map(square, numbers)

# Convert map object to list
squares = list(result)

print("Numbers:", numbers)
print("Squares:", squares)


# Using lambda
squares = list(map(lambda n: n * n, numbers))

print("Using lambda:", squares)
