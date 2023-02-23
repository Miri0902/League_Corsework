# Create a quiz with multi-choice question and display corrent or incorrect

quiz = input("What is the capital of United Kingdom?")
capital = "London"
if capital == "London":
    print("correct")
else:
    print("incorrect")



# write a program that calculates n to the power of m using multiplication only

n = int(input("Enter number 1"))
m = int(input("Enter number 2"))
ans = n
for count in range(m-1):
    ans = ans * n
print(ans)


#4. Prime number
n = int(input("Enter number"))
#prime = True
if n<2:
    print("invalid number")
for p in range(2,n):
    prime = True
    for m in range(2,p):
        if p%m == 0:
            prime = False
    if prime:
       print (p)


#5. Least Common Multiple (LCM)
n=int(input("First number"))
m=int(input("second number"))
num = 1
for num in range(1,n*m):
    if num%n == 0 and num%m == 0:
        LCD = True
    else:
        LCD = False
    if LCD:
        print(num)



