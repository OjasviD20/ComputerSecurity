# Importing libraries
import random
import hashlib

# User information to generate potential passwords
username = "laplusbelle"
name = "Marie"
surname = "Curie"
pet_name = "Woof"
birthday = "020180"
birthday_alternate = "010280"
employer = "UKC"
mother_name = "Jean_Neoskour"
father_name = "Jvaist_Fairecourir"
husband_name = "Eltrofor"
husband_birthday = "291281"
husband_birthday_alternate = "122981"

# Hash to check against
target_hash = "3281e6de7fa3c6fd6d6c8098347aeb06bd35b0f74b96f173c7b2d28135e14d45"
# Salt for hashing
salt = "5UA@/Mw^%He]SBaU"

# Function to generate password and hash for each password
def generate_and_hash_password():
    # Combine elements of user information
    elements = [username, name, surname, pet_name, birthday, birthday_alternate, employer, mother_name, father_name, husband_name, husband_birthday, husband_birthday_alternate]

    # Shuffle the elements to create diversity
    random.shuffle(elements)

    #creating password
    num_elements = random.randint(2, 5)
    password_elements = random.sample(elements, num_elements)
    password = ''.join(password_elements)

    # Hash the password with each member of the SHA family
    hashed_passwords = {}
    for sha_type in ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']:
        hasher = hashlib.new(sha_type)
        hasher.update((password + salt).encode())
        hashed_passwords[sha_type] = hasher.hexdigest()

    return password, hashed_passwords

# Function to generate passwords and check against the target hash
def generate_passwords_until_match(target_hash, max_attempts=100000):
    password_list = []
    for attempt in range(1, max_attempts + 1):
        password, hashed_passwords = generate_and_hash_password()
        password_list.append((password, hashed_passwords))

        # Check if any hash matches the target hash
        for sha_type, hashed_password in hashed_passwords.items():
            if hashed_password == target_hash:
                print(f"Password match found. The password is" , password)
                return password_list

    print("No match found within the specified number of attempts.")
    return password_list
# Generate passwords and check for a match
generated_passwords = generate_passwords_until_match(target_hash)




