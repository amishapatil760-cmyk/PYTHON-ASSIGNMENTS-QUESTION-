# Q50. Build a simple ATM menu using match case (Python 3.10+).
balance = 5000.0
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Choose an option (1-3): "))
match choice:
    case 1:
        print("Current balance: Rs.", balance)
    case 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Updated balance: Rs.", balance)
        else:
            print("Enter a valid amount")
    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            print("Please collect your cash")
            print("Remaining balance: Rs.", balance)
        else:
            print("Invalid amount or insufficient balance")
    case _:
        print("Invalid choice")
