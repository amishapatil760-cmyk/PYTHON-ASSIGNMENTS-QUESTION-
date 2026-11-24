# Q34. Check whether a string is palindrome
text = input("Enter a string: ")
cleaned = text.lower().replace(" ", "")
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
