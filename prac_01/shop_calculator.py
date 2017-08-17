number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
i = 0
total = 0
while i < number_of_items:
    price_of_item = float(input("Price of item: "))
    total = total + price_of_item
    i += 1
if total > 100:
    total = total + (total * 10 / 100)
print("Total price for " + str(number_of_items) + " items is $" + str(total))
