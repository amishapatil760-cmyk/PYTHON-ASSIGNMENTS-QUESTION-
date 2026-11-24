# Q49. Display menu-driven program using while loop
while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 4:
        print("Exiting...")
        break
    if choice in (1, 2, 3):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == 1:
            print("Result =", a + b)
        elif choice == 2:
            print("Result =", a - b)
        else:
            print("Result =", a * b)
    else:
        print("Invalid choice")
