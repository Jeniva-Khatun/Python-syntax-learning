# Local and global scope

x = 100  # Global variable


def show_scope():
    y = 50  # Local variable

    print("Inside function:")
    print("Global x:", x)
    print("Local y:", y)


show_scope()

print("Outside function:")
print("Global x:", x)

# y cannot be accessed here
# print(y)  # NameError


# Modifying a global variable using global
count = 0


def increase():
    global count
    count += 1


increase()
increase()

print("Count:", count)
