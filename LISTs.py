names = ['Mirka', 'John', 'Bob', ' Sarah', 'Mako']
print(names [0]) # using index as [0] will print the first name only

# we can use index to correct a name or a value in a list

names = ['Mira', 'John', 'Bob', ' Sarah', 'Mako']
names [0] = 'Mirka'
print(names)

#exercise, find the largest number in a list

numbers =[0, 1, 2, 4, 100, 1000]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# 2d list
# in maths we have a matrix, a 3x3 as:

# 123
# 456
# 789

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)


# List methods or functions

numbers = [5, 2, 1, 7, 4]   # to add a number
numbers.append(20)
print(numbers)

numbers = [5, 2, 1, 7, 4]   # insert a number in a specific place
numbers.insert(0, 11)    # first is position(index) and then the number itself
print(numbers)

# remove an item
numbers = [5, 2, 1, 7, 4]
numbers.remove(1)
print(numbers)

# to clear the list
numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

# pop removes the last number

numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

#to find the index of a specific number

numbers = [5, 2, 1, 7, 4]   # to add a number
print(numbers.index(5))

# to check for an existence of a number or a character in a list

numbers = [5, 2, 1, 7, 4]
print(50 in numbers)


# find the same number occurance
numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5))

# to sort a list in order in ascending order
numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()
print(numbers)

# sort a list in descending order

numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)

# copy method and creating two independent lists

numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)

# exercise
#write a progam to remove the duplicate in a list

numbers = [4, 6, 5, 4, 7, 3, 1, 5, 6, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)