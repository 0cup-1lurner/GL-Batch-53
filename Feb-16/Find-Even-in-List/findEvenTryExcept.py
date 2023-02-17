
def find_even_2(l):
    """Assumes l is a list of numbers
        Returns the first even number found
        Raises a ValueError if no even number is found
    """
    i = 0
    try:
        while l[i] % 2 != 0:
            i += 1
    except IndexError:
        raise ValueError("No even number found")
    else:
        #  Return the even number
        return l[i]
