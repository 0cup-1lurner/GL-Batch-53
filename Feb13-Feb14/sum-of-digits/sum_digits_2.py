
def sumDigits2(s):
    """Assumes s as str
         Returns sum of digits
    """
    count = 0  # Store sum of digits in count
    for i in s:
        try:
            count += int(i)
        except ValueError:
            continue

    return count

n = input("Enter a number")  # user i/p

print(sumDigits2(n))
