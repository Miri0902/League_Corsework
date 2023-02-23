
class Person:
    ''' A class person with name, address and country'''
    def __init__(self, full_name : str, address : str, country : str):
        self.name = full_name
        self.address = address
        self.country = country

    def first_name(self):
        names = self.name.split(" ")
        return names[0]

    def last_name(self):
        names = self.name.split(" ")
        return names[-1]

    def who_am_i(self):
        fn = self.first_name()
        ln = self.last_name()
        a = self.address
        c = self.country
        str = f"I am {ln}, {fn} {ln}. I live in {a}. I am from {c}."
        return str

def test_Person():

    pJB = Person("James Bond", "London, UK", "UK")
    pRH = Person("Robin Hood", "Nottingham, UK", "UK")
    pME = Person("Mirka Ezel", "London UK", "UK")
people = [pJB, pRH, pME]

print("My 'Person', objects are:")
for p in people:
    print(p.who_am_i())


from person import *

class Student(Person):
    ''' A student class, a child of 'Person'''
    def __init__(self, full_name, address, country, degree):
        super(). __init__(full_name, address, country)
        self.degree = degree

    def kind(self):
        return "student"
    def who_am_i(self):
        str = super().who_am_i()
        str = str + "I am taking a " + self.degree
        return str

from person import *

class Student(Person):
    ''' A student class, a child of 'Person'''
    def __init__(self, full_name, address, country, degree):
        super(). __init__(full_name, address, country)
        self.degree = degree

    def kind(self):
        return "student"
    def who_am_i(self):
        str = super().who_am_i()
        str = str + "I am taking a " + self.degree
        return str

from person import *

class Staff(Person):
    ''' A staff class, a child of 'Person'''
    def __init__(self, full_name, address, country, degree):
        super(). __init__(full_name, address, country)
        self.degree = degree

    def kind(self):
        return "staff"
    def who_am_i(self):
        str = super().who_am_i()
        str = str + "I am taking a " + self.degree
        return str

from person import *
from student_person import *
from staff_person import *

self present_person(p):
    print(p.who_am_i())
