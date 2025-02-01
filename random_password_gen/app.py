import random

# Alphabets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

# Numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Welcome to Password Generator:")

# Input from the user for password 
n_letters = int(input("How many letters do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))

# Empty List to store password
password_list = []

# For letters
for _ in range(n_letters):
    char = random.choice(letters)
    password_list.append(char)  # Add to password list

# For symbols
for _ in range(n_symbols): 
    char = random.choice(symbols)
    password_list.append(char)  # Add to password list

# For numbers
for _ in range(n_numbers): 
    char = random.choice(numbers)
    password_list.append(str(char))  # Add numbers as strings

# Shuffle the list to randomize the order of characters
random.shuffle(password_list)

# Convert list to string 
password = ''.join(password_list)

#print the final password: 
print(f"Your generated password is: {password}")
