# Warn after 3 unsuccessful attempts

password = "Abcd@1234"  # Disclaimer: Please use secure passwords.
for i in range(3):
    pw = input("Enter Password\n")
    if pw == password:
        print(f"Login Successful! Attempts taken {i+1}")
        break
    print(f"Enter password again.\n No. of Attempts completed = {i+1}. \n No. of attempts left = {2-i} ")

else:
    print("Suspicious activity detected")
