birth_year = input('Birth year: ')
print(type(birth_year))
age = 2023 - int(birth_year)
print(type(age))
print(age)

weight = int(input('What is your weight in pounds?: '))
result = weight * 0.5
print('my weight in kg', result)


#to create a string we use three quotes either single of double ones
# creates a multiline string

course = '''Hi John, 
Here is my first email to you.

Thank you, 
The support Team
'''
print(course)

#further example of a string - to get the first letter of the word Python

course = 'Python for Beginners'
print(course[0])

# [:] will copy whole sentence from course
course= 'Python for Beginners'
another = course[:]
print(another)

#CONVERT weight

weight = int(input("Weight"))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":    # so we can enter either L or l
    converted = weight * 0.45
    print(f'Weight in {converted} kilos')
else:
    converted = weight / 0.45
    print(f'Weight in {converted} pounds')

