import hashlib

# Function to take password and atttempt every hash type possible. 
def hash_password(password, hash_type="sha1"):
    # Choose the hash function
    if hash_type == "sha1":
        hash_function = hashlib.sha1()
    elif hash_type == "sha224":
        hash_function = hashlib.sha224()
    elif hash_type == "sha256":
        hash_function = hashlib.sha256()
    elif hash_type == "sha384":
        hash_function = hashlib.sha384()
    elif hash_type == "sha512":
        hash_function = hashlib.sha512()
    else:
        raise ValueError("Unsupported hash type")

    # Update the hash function with the password
    hash_function.update(password.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_password = hash_function.hexdigest()

    return hashed_password
#Function to compare hashes. 

def compare_hashes(input_password, known_hash, hash_type="sha1"):
    # Hash the input password
    hashed_input = hash_password(input_password, hash_type)

    # Compare the hashed input with the known hash
    return hashed_input == known_hash

# Checking given hash
known_hash = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"

#Using the phpbb text file for dictionary attack
password_file_path = 'phpbb.txt'
with open(password_file_path, 'r') as file:
   password_list = file.read().splitlines()

#Checking each password in the list until the hashed password from list matches given hash.
for password in password_list:
    # testing for different members of sha family
   for hash_type in ["sha1", "sha224", "sha256", "sha384", "sha512"]:
       if compare_hashes(password, known_hash, hash_type):
            print(f"Password Match Found. The password from the hash is '{password}'")





