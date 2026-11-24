# Q14. Check whether a character is uppercase or lowercase.
ch = input("Enter a character: ")
if len(ch) == 1 and ch.isalpha():
    if ch.isupper():
        print("Uppercase")
    else:
        print("Lowercase")
else:
    print("Please enter a single alphabet")
