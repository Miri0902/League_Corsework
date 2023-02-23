# 1. Even or Odd

number = int(input("Enter a number:"))
if number % 2 == 0:
    print("given number is even")
else:
    print("number is odd")

# to check for odd numbers

def is_odd(num):
    return num % 2 != 0

#2 multiple of. Write a program that takes two integer values from user: number 1 and number2, then
#says wheter number1 is a multiple of number2

number1 = int(input("Enter number1"))
number2 = int(input("Enter number2"))
if number2 == number1 * 2:
    print("it is a multiple")
else:
    print("number is not a multiple")

#3 Absolute
#Write a program that gives the absolute value of a number given by the user. The absolute value
#of a given number k is k itself if it is positive, and -k if it is negative

num = int(input("Enter number: "))
if num>=0:
    print(num," is positive")
else:
    print(num," is negative, the absolute value is ",num*-1)

age = 15
print("kid" if age < 18 else "adult")
