#  Write in python a recursive function sum_up_to(n) that calculates
# the sum of all natural numbers from 1 up to a given number n

def sum_up_to_k(k):
    count = 0
    j = 0
    while count <= k:
        j = j + count
        count = count + 1
    return j
print(sum_up_to_k(4))