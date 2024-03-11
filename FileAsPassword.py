# Importing Libraries
import os
import hashlib


def user_reg(users):
    # Get data from the user
    try:
        username = input("Enter User Name: ")
        password_file_path = input("Enter File Path as password : ")
        password_file = open(password_file_path,"rb")

        # Creating random salt of 8 digits
        salt = os.urandom(8).hex()

        # Appending Salt to the password
        plaintext = str(str(password_file.read()).encode())
        hashedtext = plaintext + salt

        # Hashing the password up to N4 times)
        for i in range(4):
            hashedtext = hashlib.sha256(hashedtext.encode()).hexdigest()


        # Storing the user data as variables
        users[username] = {
            'salt': salt,
            'hash': hashedtext,

        }
    except FileNotFoundError:
        print("Cannot find file at the provided file path.")


def login(users):
    try:
        login_username = input("Enter the username to login: ")
        login_password_file_path = input("Enter File Path as password : ")
        login_password_file = open(login_password_file_path,"rb")


        if login_username in users:
            user_data = users[login_username]

            # Getting salt
            salt = user_data['salt']
            temp_var = str(str(login_password_file.read()).encode()) + salt

            # Hashing the password + salt up to 4 times
            hashedtext2 = temp_var
            for i in range(4):
                hashedtext2 = hashlib.sha256(hashedtext2.encode()).hexdigest()

            # Comparing the newly hashed password with the hashed password from the variables
            if hashedtext2 == user_data['hash']:
                print("LOGIN SUCCESSFUL")
            else:
                print("LOGIN FAILED")
        else:
            print("User not found")
    except FileNotFoundError:
        print("Cannot find file at the provided file path.")

# Dictionary used to store the users
user_data_dict = {}

choice = int(input("Enter 1 to register, Enter 2 to Login, anything else to quit: "))
while (choice < 3):
    if choice == 1:
        user_reg(user_data_dict)
        loop_var = 0
        choice = int(input("Enter 1 to register, Enter 2 to Login, anything else to quit: "))
    elif choice == 2:
        login(user_data_dict)
        loop_var = 0
        choice = int(input("Enter 1 to register, Enter 2 to Login, anything else to quit: "))
    else:
        break

