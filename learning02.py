# arithmetic operations

print(10 / 3)  # this gives us a floating number
print(10 // 3) # returns an integer, whole number
print(10 % 3) # returns the remainder of the division 3 remainder 1
print( 10 ** 3) # exponent


#augmented operator
# first one is an example of normal sum
x = 10
x = x + 3
print(x)

# this can be rewritten by augmented (enhanced) perator as

x = 10
x += 3 # also works with -=
print(x)

x = (10 + 3) * 2 ** 2
print(x)

# math functions

x = 2.9
print(round(x)) # round will round up the floating number

# absolute, it returns always positive represetation of the number
x= 2.9
print(abs(-2.9))

# to get math operators we use import math and then we use math. and we get list of operators

import math

print(math.ceil(2.9)) # we get 3

import math
print(math.floor(2.9))  # we get 2 find more on python 3 math module on google


