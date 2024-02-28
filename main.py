def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * ((100 - discount_percent) / 100)
    else:
        return price


while True:
    price = int(input("Enter Price: "))
    if price > 0:
        break

while True:
    discount_percent = int(input("Enter discount percentage: "))
    if discount_percent > 0 and discount_percent < 101:
        break

print(calculate_discount(price, discount_percent))
