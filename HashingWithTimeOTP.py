# Importing Hashlib library for SHA256, and OS for random generator
import hashlib
import os
import datetime

# Function to generate a random salt
def generate_salt():
    size = 4
    return os.urandom(size).hex()

# Function to create the hash
def calculate_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to register a new account into text file
def register_account(username, password, profile_info):
    salt = generate_salt()
    hash_value = calculate_hash(password + salt)

    # Store the user record in a local file
    with open("user_file.txt", "a") as user_file:
        user_file.write(f"{username} {salt} {hash_value} {profile_info}\n")

#Function to calculate OTP using the time
def calculate_otp(hashed_password_with_time):
    return hashed_password_with_time[-12:-6]

# Function to check login credentials
def login(username, password):
    with open("user_file.txt", "r") as user_file:
        for line in user_file:
            stored_username, stored_salt, stored_hash, stored_profile_info = line.strip().split()
            if stored_username == username:
                hash_attempt = calculate_hash(password + stored_salt)
                updated_hsp = calculate_hash(stored_hash + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                stored_otp = calculate_otp(updated_hsp)
                return hash_attempt == stored_hash, stored_otp
    return False


choice = int(input("Enter 1 to register, Enter 2 to Login: "))
while (choice < 3):
    if choice == 1:
        print("Please Register Your Account")
        username1 = input("Enter a user name: ")
        password1 = input("Enter a password: ")
        AdditionalProfileInfo = input("Enter a phone number ")
        register_account(username1, password1, AdditionalProfileInfo)
        choice = int(input("Enter 1 to register, Enter 2 to Login: "))
    elif choice == 2:
        print("Please Enter Your Login Credentials ")
        login1 = input("Enter your username: ")
        password2 = input("Enter your password: ")
        creds, stored_otp = login(login1, password2)
        if creds:
            print("Login successful!")
            print("OTP you would have gotten via SMS: ", stored_otp)
            otp_input = input("Enter the OTP received via SMS: ")
            if otp_input == stored_otp:
                print("OTP verification successful!")
                choice = int(input("Enter 1 to register, Enter 2 to Login: "))
            else:
                print("OTP verification failed. Login aborted.")
                choice = int(input("Enter 1 to register, Enter 2 to Login: "))
        else:
            print("Login failed. Invalid username or password.")
            choice = int(input("Enter 1 to register, Enter 2 to Login: "))

