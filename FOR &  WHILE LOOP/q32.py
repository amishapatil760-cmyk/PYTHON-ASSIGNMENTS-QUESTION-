# Q32. Calculate power of a number without using pow()
base = float(input("Enter base: "))
exponent = int(input("Enter non-negative exponent: "))
result = 1
for _ in range(max(0, exponent)):
    result *= base
print("Result =", result)
