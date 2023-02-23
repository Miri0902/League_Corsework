# penultimate with indexing
def penultimate(l):
    if len(l)>1:
        r = l[-2] #gives 2nd to last number
    else:
        r = None
    return r


# The next two using slicing

def take(l,k):
    if len(l)>=k:
        r = l[:k]
    else:
        r = None
    return r

def tail(l):   # tail function - returns the tail of the list
    if len(l)>0:
        r = l[1:-1]
    else:
        r = None
    return r



evens = [0, 2, 6, 8]
type(evens[0])
