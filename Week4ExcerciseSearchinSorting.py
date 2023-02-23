employees = ['Li', 'John', 'Hannah', 'Alaa', 'Georgia']

def shortest(names):
    short = len(names[0])
    pos_short = names[0]
    for position, item in enumerate(names):
        if short >len(item):
            short = len(item)
            pos_short = item
    return short, pos_short

shortest_e = shortest(employees)
print(shortest (employees))
# or print(employees[shortest_e[1]])


# write a program that find the longest employees name # does to work atm
def longest(names):
    long = len(names[0])
    pos_long = names[0]
    for position, item in enumerate(names):
        if long >len(item):
            long = len(item)
            pos_long = item
    return long, pos_long


print(longest (employees))

#



