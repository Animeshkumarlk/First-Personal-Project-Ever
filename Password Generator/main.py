import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

character_list = ""

while True:
    choice = int(input("Pick a number: "))
    if choice == 1:
        character_list += string.ascii_letters
    elif choice == 2:
        character_list += string.digits
    elif choice == 3:
        character_list += string.punctuation
    elif choice == 4:
        break
    else:
        print("Please pick a valid option!")

# Generating password
password = [random.choice(character_list) for _ in range(length)]

# Printing password as a string
print("The random password is:", "".join(password))
