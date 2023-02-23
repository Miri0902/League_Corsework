long_string = """ This a string
over multiple
lines"""
print(type(long_string))
print(len(long_string))


my_book = "Book: Pride and Prejudice"
print(my_book.split())
print(my_book.split(':'))

number = int(input("please give a number between 1 an 10:"))
print(number)
print(type(number))

#FLOATS
# convert an integer to a float

x= 3
print(x)
type(x)
float_x = float(x)
print(float_x)
print(type(float_x))

# convert a string to a float
string_1 ="4.5"
string_2 = "1000000"
float_1 = float(string_1)
float_2 = float(string_2)
print(float_1)
print(type(float_1))
print(float_2)
print(type(float_2))

# calculator
# task 1
print(13//2)
print(13%2)
print(1-0.99)
print(7.5**2)

# task 2 Convert hours to minutes: input hours. Convert the value returned from a string into a number using float()
# then convert this into minutes by multiplying by 60. Print out message what time it it

hours = int(input("Enter an hour between 1 and 24"))
print(float(hours))
minutes = hours * 60
print("the time in minutes is:", minutes)

# calculator for student expenses: write a program that asks the user to enter monthly expenses one by one,
# calculates the total and displays a message indicating the total. Use float() to convert from
# string to numerical values

rent = int(input("Enter your rent"))
food = int(input("Enter your food"))
eating_out = int(input("Enter your eating out"))
travel = int(input("Enter your travel cost"))
total_expenses = rent + food + eating_out + travel
float(total_expenses)
print("Your total expenses for the month are:", total_expenses)
