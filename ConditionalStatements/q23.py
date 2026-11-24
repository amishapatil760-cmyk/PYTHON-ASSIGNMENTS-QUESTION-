# Q23. Calculate electricity bill based on units consumed.
units = float(input("Enter electricity units: "))
if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.5
    print("Electricity bill: Rs.", bill)
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
    print("Electricity bill: Rs.", bill)
else:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    print("Electricity bill: Rs.", bill)
