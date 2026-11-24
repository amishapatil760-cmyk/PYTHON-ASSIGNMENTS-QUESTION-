# Q49. Print result status using match case (Python 3.10+).
status = input("Enter result status (pass/fail/absent): ").lower()
match status:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("Result: Fail")
    case "absent":
        print("Result: Absent")
    case _:
        print("Invalid result status")
