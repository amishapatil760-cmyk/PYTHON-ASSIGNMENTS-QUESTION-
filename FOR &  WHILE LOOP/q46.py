# Q46. Print first n multiples of a number
number = int(input("Enter a number: "))
n = int(input("How many multiples? "))
for i in range(1, n + 1):
    print(number * i)
