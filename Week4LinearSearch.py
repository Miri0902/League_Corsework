#my_list = [1, 4, 7, 2, 6, 4, 3]
#val = 4
#for item in my_list:  # range(0,len(my_list))
#    if item == val:
#        found = True
#        break

     # this is more efficient

#def find_val(my_list : list, val : int):
#    for item in my_list:
#        if item == val:
#            return True

#    return False


# test
#result = find_val([1, 4, 7, 2, 6, 4, 3],4)
#print(result)


# to find the position of the item
# using enumerate() function

my_list = my_list = [1, 4, 7, 2, 6, 4, 3]
for position,item in enumerate(my_list):
    print(position, item)

my_list = my_list = [1, 4, 7, 2, 6, 4, 3]
for item in enumerate(my_list):
    print(item)


#def find_val(my_list, val):
#   for position, item in enumerate(my_list):
#       if item == val:
 #          return position
#
 #   return None

# test
#result = find_val(my_list,2)
#print(result)
#print(my_list[3])

# more eficient example


def find_val(my_list, val):
    for position, item in enumerate(my_list):
        if item == val:
            return position
        elif item>val:
            return None

    return None


# test for the above
my_list = [1, 2, 3, 6, 7, 9, 10]
result = find_val(my_list,7)
print(result)

# further example made more efficient

def find_val(my_list, val):
    for position, item in enumerate(my_list):
        print ("I am at item", item)
        if item == val:
            return position
        elif item>val:
            return None

    return None


# test for the above
my_list = [1, 2, 3, 6, 7, 9, 10]
result = find_val(my_list,7)
print(result)


# new advanced shorting
# standard algorithm check whether the number next is < or> then the one prior
#bubble sort with Isma

numbers = [90,55,7,100]
sorted_list = [7,55,90,100]

def sort_list(numbers:list)->list:
    for index in range(0,len(numbers)-1):
        print("numbers:",numbers)   # this can be left out as it only tells us if it works
        for j in range(0,len(numbers)-1-index):
            print("j:",j)    # can be left out as the above
            if numbers[j]>numbers[j+1]:
                temp = numbers[j]   # temporary assignes eg no 90 so it is not lost
                numbers[j] = numbers[j+1]
                numbers[j+1]= temp
    return numbers

print(sort_list(numbers))




