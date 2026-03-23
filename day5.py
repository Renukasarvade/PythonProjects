# password genrator
import random
import string

length = int(input("Enter length: "))

characters = string.ascii_letters + string.digits

password = ""

for _ in range(length):
    password += random.choice(characters)

print("Password:", password)


import random

# generate lottery numbers
lottery = [random.randint(1, 50) for _ in range(3)]

# user input
user = []
for i in range(3):
    num = int(input(f"Enter number {i+1}: "))
    user.append(num)

# compare
matches = 0
for num in user:
    if num in lottery:
        matches += 1

# output
print("Lottery:", lottery)
print("Your numbers:", user)
print("Matches:", matches)