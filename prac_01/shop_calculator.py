n = int(input("Number of items: "))
sum = 0

if n > 0:
    for num in range(0, n, 1):
        price = float(input("Price of item: "))
        sum = sum + price
    if sum > 100:
        discount = 10/100 * sum
        print("Total price for {} items is $".format(n), sum - discount)
    else:
        print("Total price for {} items is $".format(n), sum)

else:
    print("Invalid number of items!")
    n = int(input("Number of items: "))
