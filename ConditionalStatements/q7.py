# Q7. Check whether a character is a vowel or consonant.
ch = input("Enter an alphabet: ").lower()
if len(ch) == 1 and ch.isalpha():
    if ch in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Please enter a single alphabet")
