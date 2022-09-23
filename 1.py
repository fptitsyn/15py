def d(a, b):
    return a % b == 0


count = 0

for a in range(1, 1000):
    for x in range(1, 1000):
        if not (d(a, 25) and (d(x, 24) and d(x, 75)) <= d(x, a)):
            break
    else:
        print(a)
        count += 1

print(count)
