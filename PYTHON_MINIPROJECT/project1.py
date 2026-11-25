# Mini Project 1: Text Analyzer System

text = input("Enter a sentence or paragraph: ")

# Remove extra spaces
text = " ".join(text.split())

# Count characters, words and sentences
characters = len(text)
words = text.split()
sentences = 0

for ch in text:
    if ch in ".!?":
        sentences += 1

if text and sentences == 0:
    sentences = 1

# Count vowels, consonants, digits and special characters
vowels = 0
consonants = 0
digits = 0
special = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        special += 1

# Convert text
print("\nUppercase:", text.upper())
print("Lowercase:", text.lower())

# Check whether a word exists
search_word = input("\nEnter a word to search: ")
if search_word.lower() in [word.lower() for word in words]:
    print("Word exists")
else:
    print("Word  not exist")

# Find frequency of each word
print("\nWord frequency:")
for word in set(words):
    print(word, ":", words.count(word))

# Display analysis
print("\nTotal characters:", characters)
print("Total words:", len(words))
print("Total sentences:", sentences)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)
print("Text without extra spaces:", text)
