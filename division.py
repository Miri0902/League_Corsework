# write a program that does the integer division of two integers p and q using substraction only

numberP = int(input("enter number 1"))
numberQ = int(input("enter number 2"))
totalNumber = 0

for i in range(numberQ):
    totalNumber -= numberP

print(numberP, " / ", numberQ, " = ", totalNumber)


p= int(input("First number"))
q = int(input("Second number"))
quotient = 0
remainder = 0
while quotient <1000:
    if p<q:
        remainder = p
        break
    else:
        p = p-q
        quotient = quotient + 1
print(quotient,"r ",remainder)

