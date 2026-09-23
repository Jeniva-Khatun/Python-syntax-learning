#recursive function -> a function calling itself repeatedly

n=int(input("enter a no : "))
def factorial(n):
    if n==0 or n==1:
        return 1

    return  n * factorial(n-1)

print("factorial is : ",factorial(n))
