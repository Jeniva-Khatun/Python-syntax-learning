age = int(input("enter your age : "))
has_id = True

if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("ID is required")
else:
    print("You are under 18")
