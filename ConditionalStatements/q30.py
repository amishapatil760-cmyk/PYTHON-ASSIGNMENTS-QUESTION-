# Q30. Check the type of number (single, double, or three digit).
n = abs(int(input("Enter an integer: ")))
if n <= 9:
    print("Single-digit number")
elif n <= 99:
    print("Double-digit number")
elif n <= 999:
    print("Three-digit number")
else:
    print("More than three digits")
