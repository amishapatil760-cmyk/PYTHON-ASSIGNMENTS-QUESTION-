# Mini Project 2: Password Strength Checker

password = input("Enter a password: ")

# Check password conditions
has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

# Display checks
print("Minimum length (8):", len(password) >= 8)
print("Uppercase letter:", has_upper)
print("Lowercase letter:", has_lower)
print("Digit:", has_digit)
print("Special character:", has_special)

# Check password strength
score = 0

if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if score == 5:
    print("Password Strength: Strong")
elif score >= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")
