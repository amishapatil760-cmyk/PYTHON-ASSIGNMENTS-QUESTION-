# Q40. Check whether a password is valid using nested if.
password = input("Enter password: ")
if len(password) >= 8:
    if any(ch.isdigit() for ch in password):
        print("Valid password")
    else:
        print("Password must contain at least one digit")
else:
    print("Password must contain at least 8 characters")
