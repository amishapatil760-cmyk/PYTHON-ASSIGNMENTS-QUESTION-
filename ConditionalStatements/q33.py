# Q33. Check whether a person can apply for a loan.
age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
if age >= 21 and age <= 60:
    if salary >= 25000:
        print("Meets the basic loan application criteria")
    else:
        print("Does not meet the salary criterion")
else:
    print("Does not meet the age criterion")
