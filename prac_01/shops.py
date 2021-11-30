for i in range(1, 21, 2):
    print(i, end=' ')

print("\n")

for x in range(0, 101, 10):
    print(x, end=' ')

print("\n")

for n in range(20, 0, -1):
    print(n, end=' ')

print("\n")

stars_1 = int(input("Number of stars: "))

for m in range(0, stars_1, 1):
    print("*", end=' ')

print("\n")

for v in range(0, stars_1, 1):
    for j in range(0, v + 1):
        print('*', end=' ')
    print("\r")
