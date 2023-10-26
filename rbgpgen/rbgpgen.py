#Generates a random password with a length of your choice
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("Enter password length: "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)


    password = "".join(password)

    print(password)


option = input("Generate password? (y/n): ")

if option == "y":
    generate_password()
elif option == "n":
    print("Goodbye!")
    quit()
else:
    print("Invalid option!")
    quit()
