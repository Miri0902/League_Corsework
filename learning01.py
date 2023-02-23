# formatted strings

course =('Python for Beginners')
print(len(course))

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder' # this is concatenated string, which is not user friendly as is too long
# hence we will format it using the folowing
msg = f'{first} [{last}] is a coder ' # this is formated string using 'f'
print(message)

#string methods - using dot ' . ' operator

course = 'Python for beginners'
print(course.upper())
print(course)

course = 'Python for beginners'
print(course.lower())
print(course)

course = 'Python for beginners'
print(course.find('P')) # we get 0 as the index of P is 0 and returns index

course = 'Python for beginners'
print(course.replace('beginners', 'Absolute Beginners'))
print(course)

#to check the existence of a character in a string

course = 'Python for beginners'
print('Python' in course) # returns Boolean expression True or False







