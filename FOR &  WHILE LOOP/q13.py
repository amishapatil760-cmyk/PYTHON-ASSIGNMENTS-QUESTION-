# Q13. Check whether a number is palindrome
n = int(input("Enter a number: "))
original = n
temp = abs(n)
reverse = 0
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
if n >= 0 and original == reverse:
    print("Palindrome")
else:
    print("Not palindrome")
