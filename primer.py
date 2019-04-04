def mean(set):
    """Takes a list of of objects and attempts to find the mean"""
    s = 0
    for n in set:
        s = n + s

    m = s / len(set)

    return m


def median(set):
    """Returns the median value of a set"""
    
    set.sort()
    width = len(set)
    middle_val = int(width / 2)
 
    if (width % 2) == 0:
        m = set[middle_val - 1] + set[middle_val]
        m = m / 2
        return m
    else:
        m = set[middle_val]
        return m

def mode(set):
    """Returns the number with the most occurences in a set."""
    
    # To get the mode we need to look for numbers that occur more than once in
    # the set. We could store number / occurence pairs in a dict. Or we could 
    # store the the values in two variables. Check all numbers against each
    # each value in a set and save the values that have the highest count.
    # Or we could construct lists of the occurences of each value and check the
    # length of the list.

    set.sort()
    

    

def even(n):
    """Returns True if parity of number is even, false if odd."""
    if (n % 2) == 0:
        return True
    else:
        False