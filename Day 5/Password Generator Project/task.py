import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Generating the password using loops

# Easy level password generation
password = ""
if nr_letters !=0:
    for letter in range(nr_letters):
        random_letter = random.choice(letters)
        password += str(random_letter)
if nr_symbols !=0:
    for symbol in range(nr_symbols):
        random_symbol = random.choice(symbols)
        password += str(random_symbol)
if nr_numbers !=0:
    for number in range(nr_numbers):
        random_number = random.choice(numbers)
        password += str(random_number)

print(f"Your easy password is : {password}\n")

# Hard level password generation
password =""
password_list = []
for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

for char in password_list:
    password += char

print(f"\nYour Strong password is : {password}")
