# Q46. Print grade description using match case (Python 3.10+).
grade = input("Enter grade (A/B/C/F): ").upper()
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very good")
    case "C":
        print("Good")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")
