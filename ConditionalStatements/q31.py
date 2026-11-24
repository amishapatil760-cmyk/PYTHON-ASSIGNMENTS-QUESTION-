# Q31. Check whether a number is positive and even using nested if.
n = int(input("Enter a number: "))
if n > 0:
    if n % 2 == 0:
        print("Positive and even")
    else:
        print("Positive but odd")
else:
    print("Number is not positive")
