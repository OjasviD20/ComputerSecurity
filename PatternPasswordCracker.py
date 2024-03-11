import itertools
import hashlib

# Generating all possible patterns
def generate_patterns():
    letters = "abcdefghi"
    patterns = []
    # Generate patterns of different lengths and making sure no letter is used more than once.
    for length in range(1, 10):
        for perm in itertools.permutations(letters, length):
            pattern = "".join(perm)
            patterns.append(pattern)

    return patterns

# Hashing letter pattern.
def hash_pattern(pattern):
    sha1 = hashlib.sha1()
    sha1.update(pattern.encode('utf-8')) # convert letters in byte array pattern
    return sha1.hexdigest()

# Finding a hash that matches the given hash.
def find_matching_pattern(target_hash):
    patterns = generate_patterns()

    for pattern in patterns:
        hashed_pattern = hash_pattern(pattern)
        if hashed_pattern == target_hash:
            return pattern

    return None

# Target hash value
target_hash = "91077079768edba10ac0c93b7108bc639d778d67"

# Find the matching pattern
matching_pattern = find_matching_pattern(target_hash)

# Display the result
if matching_pattern:
    print(f"Matching pattern found: {matching_pattern}")
else:
    print("No matching pattern found.")
