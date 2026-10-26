
file = open('youtube.txt','w')

try:
    file.write('home sweet home')
finally:
    f.close()



with open('youtube.txt','w') as file:
    file.write('home is always best')