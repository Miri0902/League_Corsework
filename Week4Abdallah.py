# q3 Write a python program that creates two new lists: employees_desc and employees_asc
# that contain the strings from list employees sorted from longest to shortest (shortest to longest respectively),
# according to the number of characters of each string.

employees = ['Li', 'John','Hannah','Alaa','Georgia']

def employees_desc(name:list)->list:
    for i in range(0, len(name)-1):
        for j in range(0, len(name)-1-i):
            if len(name[j])<len(name[j+1]):
                temp = name[j]
                name[j] = name[j + 1]
                name[j+1] = temp
    return name
print("desc ", employees_desc(employees))

def employees_asc(name:list)->list:
    for i in range(0, len(name)-1):
        for j in range(0, len(name) - 1 - i):
            if len(name[j]) > len(name[j + 1]):
                temp = name[j]
                name[j] = name[j + 1]
                name[j + 1] = temp
    return name
print("asc ", employees_asc(employees))



# q4 Extend your program by writing a function sort_strings(string_list,order) where string_list is
# a list of strings and order is a variable that indicates the order in which we want to have the list sorted.
# Test it using list employees.


def sort_strings(string_list: list, order) -> list:
    if order == "desc":
        for i in range(0, len(string_list) -1):
            for j in range(0, len(string_list) -1 - i):
                if len(string_list[j]) < len(string_list[j + 1]):
                    temp = string_list[j]
                    string_list[j] = string_list[j + 1]
                    string_list[j + 1] = temp
            return string_list
    elif order == "asc":
        for i in range(0, len(string_list) -1):
            for j in range(0, len(string_list) -1 - i):
                if len(string_list[j]) > len(string_list[j + 1]):
                   temp = string_list[j]
                   string_list[j] = string_list[j + 1]
                   string_list[j + 1] = temp

            return string_list
        else:
            raise ValueError("Invalid order")
print("Employees Descending ", sort_strings(employees,"desc"))
print("Employees Ascending ", sort_strings(employees,"asc"))


# q 5 We want to add a new employee "Paul" to the list, while keeping it sorted.
# Propose an algorithm to do that without using the insert() method

def Add_and_Sort(original: list, new_name: list, order)->list:
    string_list = original + new_name
    if order == "desc":
        for i in range(0, len(string_list)-1):
            for j in range(0, len(string_list)-1 -i):
                if len(string_list[j]) < len(string_list[j + 1]):
                    temp = string_list[j]
                    string_list[j] = string_list[j + 1]
                    string_list[j + 1] = temp
        return string_list
    elif order == "asc":
         for i in range(0, len(string_list) - 1):
             for j in range(0, len(string_list) - 1 - i):
                 if len(string_list[j]) > len(string_list[j + 1]):
                     temp = string_list[j]
                     string_list[j] = string_list[j + 1]
                     string_list[j + 1] = temp

         return string_list
    else:
         raise ValueError("Invalid order")
print(Add_and_Sort(employees,["Paul"], "desc"))




