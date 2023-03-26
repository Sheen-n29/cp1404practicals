

items = int(input("Number of items: "))
total = 0

while items < 0:
    print("Invalid number of items!")   
    items = int(input("Number of items: ")) 

for i in range(items):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    discount = total * 10/100
    total = total - discount
    print(f"Total price for {items} items is {total:.2f}")
else:
    print(f"Total price for {items} items is {total:.2f}")