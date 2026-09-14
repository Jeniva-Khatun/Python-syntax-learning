

for i in range(5,0,-1):
    #space
    for j in range(5-i):
        print(" ", end="")

    #star
    for j in range(2*i-1):
       print("*",end="")

    print()
