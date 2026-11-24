# Q28. Check whether a number is Armstrong
n = int(input("Enter a number: "))
digits = str(abs(n))
power = len(digits)
total = 0
for ch in digits:
    total += int(ch) ** power
if n >= 0 and total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
