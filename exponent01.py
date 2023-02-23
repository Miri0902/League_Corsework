# Write function 'head' which returns the head of the given list


def head(l):
    r = l[0]
    return r

def head (l):
    if not(is_empty(l)):
        r = l[0]
    else:
        r = None