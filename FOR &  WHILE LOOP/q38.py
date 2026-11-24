# Q38. Find smallest digit in a number
n = abs(int(input("Enter a number: ")))
smallest = 9
if n == 0:
    smallest = 0
while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10
print("Smallest digit =", smallest)
