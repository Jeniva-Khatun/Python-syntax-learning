#lambda function
# syntax :  lamda argument : expression

add = lambda a, b: a+b

print("sum : ", add(10,20))


square = lambda a: a * a

print("square : ", square(5))

# Lambda with condition

maximum = lambda a, b: a if a > b else b

print("maximum : ", maximum(25,78))
