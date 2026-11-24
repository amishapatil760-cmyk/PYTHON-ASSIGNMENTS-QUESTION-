# Q47. Check user role using match case (Python 3.10+).
role = input("Enter role (admin/user/guest): ").lower()
match role:
    case "admin":
        print("Administrator access")
    case "user":
        print("Standard user access")
    case "guest":
        print("Guest access")
    case _:
        print("Unknown role")
