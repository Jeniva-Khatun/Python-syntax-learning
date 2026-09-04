# 1. Print numbers from 1 to 20 but skip even numbers

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)
