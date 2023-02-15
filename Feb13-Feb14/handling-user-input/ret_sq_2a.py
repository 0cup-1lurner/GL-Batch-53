
def readInt():
    """Reads input from user
          Returns sq if it is an int
"""
    while True:
        n = input("Enter a num\n")
        try:
            n = int(n)
            print("sq = ", n**2)
            break  # exit loop as user has given numerical i/p
        except ValueError:
            print(n, "is not an int")
            

