#Write a function that takes as parameter a tuple (values, element) which returns True if the element a is present
# in the list values, and False if not.

fruit = ("apple", "bananas", "pear", "grape")
item = input("please input a fruit")
if  item in fruit:
    print("True")
else:
    print("False")

# Write a function removeDuplicates(values) that finds and removes duplicate elements from list values

duplicates = (1,1,2,3,4,5,5,6,7,8,8,9)
duplicates = list(dict.fromkeys(duplicates))
print(duplicates)



values = [1,2,3,4,4,5,5,6,7,7]
def removeDuplicates(z):
    for i in z:
        if z.count(i)>1:
            z.remove(i)
            removeDuplicates(z)
            return z
print(removeDuplicates(values))

# 3. Write a function commonElements(list1,list2) which finds and returns
# all common elements between list1 and list2.

list1 = ["apples", "bananas", "oranges", "pear"]
list2 = ["apples", "pear", "kiwi", "grapes"]
def commonElements(list1, list2):
    result = [i for i in list1 if i in list2]
    return result
print("the common elements are:", commonElements(list1, list2))


# Python program to find the common elements
# in two lists
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
common_member(a, b)

# 4 Write a function myNumbers(values) that takes as parameter a list of integers values,
# and returns a list of tuples. Each tuple contains an integer and either 'odd' or 'even',
# Example:
# myNumbers([3,6,1,12]) should return [(3,'odd'),(6,'even'),(1,'odd'),(12,'even')]

myNumbers = (3,7,4,99,12,14)

def myNumbers(z):
    for i in z:
      if i in z:
        x = tuple(myNumbers)
        if z == 0:
            print(myNumbers, "even")
        elif z == 0:
         print(myNumbers, "odd")
    else:
        print("end")

# task 5 Write in python function descending (n, m) which returns a list of integers from integer n to m
# (both inclusive) in descending order. Example: descending (2, 4) should return [4, 3, 2].


#def descending(n,m):
nums = [1, 5, 3, 4, 2, 10, 6, 8, 7, 9]
nums.sort()
print('List in Ascending Order: ', nums)

nums.sort(reverse=True)
print('List in Descending Order: ', nums)





