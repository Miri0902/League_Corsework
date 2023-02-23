# write a program that multiplies two numbers n and m using addition only


numberN= int(input("enter number 1"))
numberM = int(input("enter number 2"))
totalNumber = 0

for i in range(numberM):
    totalNumber += numberN

print(numberN, " * ", numberM, " = ", totalNumber)




