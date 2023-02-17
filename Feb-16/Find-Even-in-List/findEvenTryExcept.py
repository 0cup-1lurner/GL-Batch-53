
def find_even_2(l):
    """Assumes l is a list of numbers
        Returns the first even number found
        Raises a ValueError if no even number is found
    """
    i = 0
    try:
        while l[i] % 2 != 0:
            i += 1  # Continue to check the next element in the list if l[i] is odd
    except IndexError:
	# List index out of range as i >= len(l) if no even number is present
        raise ValueError("No even number found")
    else:
        # Return the first even number
        return l[i]
