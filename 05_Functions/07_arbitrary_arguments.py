# Arbitrary arguments
# *args -> multiple positional arguments
# **kwargs -> multiple keyword arguments

def numbers(*args):
    print("argument : ", args)


    for numbers in args:
        print(numbers)

numbers(10,20,30)


def details(**kwargs):
    print("Details:", kwargs)

    for key, value in kwargs.items():
        print(key, ":", value)


details(
    name="Jeniva",
    age=20,
    course="CSE"
)
