for item in 'Python':
    print(item)

for item in ['Mirka', 'Nada' , 'Lenka']:   # list is defined by []
    print(item)

for item in range(5, 10, 2): #range function
    print(item)

# calculate the total cost of all items in a shopping cart
prices = [10, 20, 30]

total = 0
for price in prices:
    total = total + price  # or total += price
print(f"Total: {total}")


