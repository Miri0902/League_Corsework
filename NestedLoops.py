#(x, y)
#(0, 0)
#0, 1)
#(0, 2)
#(1, 0)

#basic
for x in range(4):
    print(x)

# nested loop used for getting coordinates
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')


# exercise

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

# more advanced using for loop
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
