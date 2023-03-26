for i in range(1, 21, 2):
    print(i, end=' ')
print()

for x in range(0, 101, 10):
    print(x, end =' ')
print()

for y in range(20, 0, -1):
    print(y, end = ' ')
print()

stars = int(input("Number of stars: "))
for z in range(stars):
    print("*", end='')
print()

for z in range(stars):
    for j in range(z + 1):
        print("*", end='')
    print()


