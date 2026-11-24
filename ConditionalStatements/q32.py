# Q32. Check exam eligibility based on attendance and marks.
attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))
if attendance >= 75:
    if marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible: marks are below the required level")
else:
    print("Not eligible: attendance is below 75%")
