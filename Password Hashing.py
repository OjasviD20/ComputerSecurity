# Importing Hashlib library for SHA256, and OS for random generator
import hashlib
import os

# Function to generate a random salt of given size
def generate_salt(size):
    return os.urandom(size).hex()

# Function to create the hash by combining password and salt then using SHA 256
def calculate_hash(password, salt):
    combined = password + salt
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()

# Function to register a new account into text file.
# Takes user name and password, calls salt and hash function.
# then stores everything in text file.
def register_account(username, password, profile_info):
    salt = generate_salt(5)
    hash_value = calculate_hash(password, salt)

    # Store the user record in a local file
    with open("user_file.txt", "a") as user_file:
        user_file.write(f"{username} {salt} {hash_value} {profile_info}\n")

# Function to check login credentials
# Opens text file, looks for user. Then hashes given password to compare with stored hash.
def login(username, password):
    with open("user_file.txt", "r") as user_file:
        for line in user_file:
            stored_username, stored_salt, stored_hash, stored_profile_info = line.strip().split()
            if stored_username == username:
                hash_attempt = calculate_hash(password, stored_salt)
                return hash_attempt == stored_hash
    return False

# Prompting user. 
choice = int(input("Enter 1 to register, Enter 2 to Login, anything else to quit: "))
while (choice < 3):
    if choice == 1:
        print("Please Register Your Account")
        username1 = input("Enter a username: ")
        password1 = input("Enter a password: ")
        register_account(username1, password1, "AdditionalProfileInfo")
        choice = int(input("Enter 1 to register, Enter 2 to Login: "))
    elif choice == 2:
        print("Please Enter Your Login Credentials ")
        login1 = input("Enter your username: ")
        password2 = input("Enter your password: ")
        if login(login1, password2):
            print("Login successful!")
            choice = int(input("Enter 1 to register, Enter 2 to Login: "))
        else:
            print("Login failed. Invalid username or password.")
            choice = int(input("Enter 1 to register, Enter 2 to Login: "))
    else:
        break
    
