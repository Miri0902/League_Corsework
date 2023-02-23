# tuples cannot be modified - unmutable - we have only count or index

numbers = (1, 2, 3)
print(numbers[0])

#we can change tuple to a list and then back

x = ("apple", "pear", "oranges")
y = list(x)
y[1] = "grapes"
x = tuple(y)
print(x)

# unpacking feature

coordinates = (1, 2, 3) # rather than using name of the variable all the time, we can assign a new
x = coordinates [0]     # variable
y = coordinates [1]
z = coordinates [2]
print(x, y, z)

# the above can be shorted as and can be also used with list [], as tuples ()
coordinate = (1, 2, 3)
x, y, z = coordinates
print(x)

# dictionries - we use to store key value pairs
#attribues and key values
#Name: John Smith
#Email: john@gmail.com
#Phone: 1234

# we define a dictionary using curly {}
customer = {
    "name":  "John Smith",
    "age":  30,
    "is_verified": True
}
print(customer["name"]) # this will work, but if we mispell or use invalid attribte it will give an error
                        # hence we do the following

customer = {
    "name":  "John Smith",
    "age":  30,
    "is_verified": True
}
print(customer.get("birthdate", "Jan 1 1980"))  # will return None, by addig a date it will be used as default value

# we can update the list
customer = {
    "name":  "John Smith",
    "age":  30,
    "is_verified": True
}
customer["name"] = "Jack Sparrow"
print(customer["name"])

customer = {
    "name":  "John Smith",
    "age":  30,
    "is_verified": True
}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

# exercise, change digits 1 2 3 4 into words
phone = input("Phone")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

