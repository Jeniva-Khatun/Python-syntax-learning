
pet = "dog"
age = 3

if pet == "dog":
    if age <= 2:
        print("give puppy food")
    else:
        print("give senior dog food")   

elif pet == "cat":
    if age >= 5:
        print("give senior cat food")
    else:
        print("give baby kitten food")

else:
    print("cannot verify the animal")