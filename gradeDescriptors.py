#write a program that takes a number between 0 and 16 from the user, and displays the
#corresponding grade descriptor according to the table in week1 activities

grade = int(input("Enter a grade"))
if grade == 0:
    print("Zero")
elif grade == 1:
     print("low fail")
elif grade == 2:
    print("mid fail")
elif grade == 3:
    print("marginal fail")
elif grade == 4:
    print("low 3rd")
elif grade == 5:
    print("mid 3rd")
elif grade == 6:
    print("high 3rd")
elif grade == 7:
    print("low 2:2")
else:
    if grade == 8:
        print("mid 2:2")



# the same question, however, if the user enters 8 it should say Second instead of mid 2:2

mark=int(input("Enter mark: "))
if mark==0:
    print("Zero")
elif mark >=1 and mark <=3:
    print("Fail")
elif mark >=4 and mark <=6:
    print("3rd")
elif mark>=7 and mark<=9:
    print("2 : 2")
elif mark>=10 and mark<=12:
    print("2 : 1")
elif mark>=13 and mark<=16:
    print("First")
else:
    print("Invalid Mark")