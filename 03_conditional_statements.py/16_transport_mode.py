
distance = int(input("enter the distance of your choice : "))

if distance <= 3:
    transport = "walk"
elif distance <= 15:
    transport = "bike"
else:
    transport= "car"

print("ai recommends you the transport of : ", transport )             