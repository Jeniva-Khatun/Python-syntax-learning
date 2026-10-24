
def debugg(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args )
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)

    return wrapper    

@debugg
def hello():
    print("hello")

hello()


@debugg
def greet(name, greeting= "greet with anything"):
    print(f"{greeting} , {name}")

greet("Jeniii..",greeting="hiiii")    