
def sumDigits(s):
    """Assumes s as str
         Returns sum of digits
    """
    count = 0  # Store sum of digits in count
    for i in s:
        if i.isdigit():
            count += int(i)
    return count

n = input("Enter a number")  # user i/p

print(sumDigits(n))
