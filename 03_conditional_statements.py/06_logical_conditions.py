age = int(input("Enter age : "))
has_id = True

if age >= 18 and has_id:
    print("Allowed")

if age < 18 or not has_id:
    print("Not allowed")
