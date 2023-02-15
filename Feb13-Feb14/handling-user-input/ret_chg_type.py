
def readValue(requestMsg, changeType, errorMsg):
    """Reads input from user
       Returns after changing the type or else returns apt msg
    """
    while True:
        n = input(requestMsg)
        try:
            n = changeType(n)
            return n
        except ValueError:
            print(n, errorMsg)
            

