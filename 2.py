count = 0

for a in range(1, 1000):
    for x in range(1, 1000):
        if not (x & 13 == 0) <= ((x & 40 != 0) <= (x & a != 0)):
            break
    else:
        print(a)
        break

