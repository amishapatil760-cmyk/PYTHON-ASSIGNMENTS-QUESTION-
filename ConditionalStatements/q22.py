# Q22. Check salary bonus based on years of service.
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))
if years >= 10:
    bonus = salary * 0.10
elif years >= 5:
    bonus = salary * 0.05
else:
    bonus = salary * 0.02
print("Bonus: Rs.", bonus)
