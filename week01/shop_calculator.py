total = 0
DISCOUNT = 0.1
num_item = int(input("Number of items: "))
while num_item < 0:
    print("Invalid number of items.")
    num_item = int(input("Number of items: "))
for i in range(num_item):
    price = float(input("Price of item: "))
    total += price
discounted_price = total - (total * DISCOUNT)
if total > 100:
    print(f"Total price for {num_item} items is ${discounted_price:,.2f}")
else:
    print(f"Total price for {num_item} items is ${total:,.2f}")
