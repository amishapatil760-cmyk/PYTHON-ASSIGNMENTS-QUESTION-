# Q28. Calculate discount based on total shopping amount.
amount = float(input("Enter shopping amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0
print("Discount: Rs.", discount)
print("Final amount: Rs.", amount - discount)
