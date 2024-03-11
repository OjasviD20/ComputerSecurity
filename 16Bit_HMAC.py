import hmac
import hashlib
import random

def generate_16_bit_hmac(key, message):

    # Calculating full mac with sha 256
    full_hmac = hmac.new(key.encode(), message.encode(), hashlib.sha256).digest()

    # Truncating returned mac by 16 bits
    truncated_hmac = full_hmac[:2]

    return truncated_hmac

shared_secret = "Shared Secret Key"
message = "Alice, Bob, $10"
print("Shared Secret Key is: ", shared_secret)
print("Original Message is: ", message)
new_hmac = generate_16_bit_hmac(shared_secret, message)
print("16-bit HMAC (hex):", new_hmac.hex())


max_attempts = 2**16
attempts = 0
while attempts < max_attempts:
    new_amount = random.randint(1, max_attempts)
    manipulated_message = f"Alice, Eve, ${new_amount}"
    hmac_check = generate_16_bit_hmac(shared_secret, manipulated_message)
    if hmac_check == new_hmac:
        print("HMAC match found after ", attempts, " attempts")
        print("Manipulated message is ", manipulated_message)
        print("Manipulated HMAC is", hmac_check.hex())
        break
    attempts += 1



