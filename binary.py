#1. Prime
def prime_number(n):
    if n<2:
        print("invalid number")
    for p in range(2,n):
        prime = True
        for m in range(2,p):
            if p%m == 0:
                prime = False
        if prime:
            print(p)


n=int(input("input number"))
prime_number(n)

#1. LCM
def LCD_1(n,m):
    for num in range(1,n*m):
        if num%n == 0 and num%m == 0:
            LCD = True
        else:
            LCD = False
        if LCD:
            print(num)


n=int(input("First number"))
m=int(input("second number"))
LCD_1(n,m)

# Write a function binary(n) that takes a positive integer n as input,
# and returns its binary representation as a list.

def binary(num):
    mylist = []
    aaa = num
    while num != 0:
        if num % 2 == 1:
            mylist.append(1)
            num = (num - 1) / 2
        else:
            mylist.append(0)
            num = num / 2
    mylist.reverse()
    print(aaa,"in binary is ",mylist)

num = int(input("Enter number"))
binary(num)