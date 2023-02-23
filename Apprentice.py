from UNIexerciseThursdayNuno import *

class Apprentice(Person):

     def __init__(self, full_name, position, degree):
         self.full_name = full_name
         self.postion = position
         self.degree = degree

Person2 = Person("Mirka", "Analyst", "BSc")

print(Person2)

