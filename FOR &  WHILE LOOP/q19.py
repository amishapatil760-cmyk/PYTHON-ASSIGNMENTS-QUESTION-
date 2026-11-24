# Q19. Check whether a number is prime
n = int(input("Enter a number: "))
is_prime = n >= 2
for i in range(2, int(max(n, 0) ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not prime")
