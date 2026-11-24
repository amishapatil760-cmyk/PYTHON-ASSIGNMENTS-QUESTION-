# Q24. Check exam result (Distinction, First Class, Pass, Fail).
marks = float(input("Enter marks out of 100: "))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
