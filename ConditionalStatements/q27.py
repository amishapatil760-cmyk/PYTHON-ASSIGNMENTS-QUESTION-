# Q27. Check login status based on username and password.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "student":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Username not found")
