# This is a program that calculates class average
#def grade_avg(grades):
grade_sum = 0
# assuming that we have 5 students
for i in range(5):
    grades = float(input("Please enter a grade: "))
    grade_sum = grade_sum + grades
average = grade_sum/5
print("Class average: ", average)




n = int(input("First number: "))
m = int(input("Second number: "))
ans = 0
for count in range(m):
    ans = ans + n
print(ans)
