# 3. Keep taking numbers until the user enters 0
#
#
while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    print("You entered:", num)
