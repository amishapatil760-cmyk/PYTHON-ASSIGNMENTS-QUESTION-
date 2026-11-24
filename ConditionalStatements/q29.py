# Q29. Check blood donation eligibility based on age and weight.
age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))
if age >= 18 and age <= 65 and weight >= 50:
    print("Meets the basic age and weight criteria")
else:
    print("Does not meet the basic age and weight criteria")
