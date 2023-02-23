# Program that calculates all prime number starting from 1 up to a value n, given by the user.
# 1. if the user inputs a number below 2, print an error message
# print out each number that cannot be devided by any other number - using nested loops

num = 17
#define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
