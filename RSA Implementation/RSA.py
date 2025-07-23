import sys
import math
import random

# ---------------------- Helper Functions ----------------------

def gcd(a, b):
    # Compute the greatest common divisor using Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    # Extended Euclidean algorithm to find modular inverse
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    # Compute modular inverse of a under modulo m
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

def is_prime(num):
    # Simple primality test
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# ---------------------- RSA Core ----------------------

def generate_keys(p, q):
    # Generate RSA public and private keys from primes p and q
    n = p * q
    z = (p - 1) * (q - 1)
    if n < 128:
        raise ValueError(f"Modulus n={n} is too small - choose larger primes (minimum n ≥ 128)")

    # Choose a small odd integer e such that gcd(e, z) = 1
    for e in [3, 5, 17, 65537]:
        if 1 < e < z and gcd(e, z) == 1:
            break
    else:
        # If none found, choose a random one
        possible_es = [i for i in range(2, z) if gcd(i, z) == 1]
        if not possible_es:
            raise ValueError("No valid e found")
        e = random.choice(possible_es)

    # Compute the modular inverse of e
    d = modinv(e, z)
    if d is None:
        raise ValueError("Modular inverse doesn't exist")

    return n, z, e, d

def rsa_encrypt(message, e, n):
    # Encrypt each character in the message using public key (e, n)
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(ciphertext, d, n):
    # Decrypt each number in the ciphertext using private key (d, n)
    return ''.join([chr(pow(c, d, n)) for c in ciphertext])

# ---------------------- File IO ----------------------

def save_keys(n, e, d):
    # Save public and private keys to files
    with open("public_key.txt", "w") as f:
        f.write(f"{n} {e}\n")
    with open("private_key.txt", "w") as f:
        f.write(f"{n} {d}\n")

def load_public_key():
    # Load public key from file
    with open("public_key.txt") as f:
        n, e = map(int, f.read().split())
    return n, e

def load_private_key():
    # Load private key from file
    with open("private_key.txt") as f:
        n, d = map(int, f.read().split())
    return n, d

def save_message(ciphertext):
    # Save encrypted message to file
    with open("message.txt", "w") as f:
        f.write(' '.join(map(str, ciphertext)))

def load_message():
    # Load encrypted message from file
    with open("message.txt") as f:
        return list(map(int, f.read().split()))

# ---------------------- Menu System ----------------------

def menu():
    # Display the main menu and handle user choices
    while True:
        print("\n===== RSA Secure Mail System =====")
        print("1. Generate RSA Keys")
        print("2. Send Encrypted Message")
        print("3. Read & Decrypt Message")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # Generate RSA keys from two primes
            p = int(input("Enter prime p: "))
            q = int(input("Enter prime q: "))
            if not is_prime(p) or not is_prime(q) or p == q:
                print("Both numbers must be distinct primes.")
                continue
            try:
                n, z, e, d = generate_keys(p, q)
                save_keys(n, e, d)
                print(f"Keys generated and saved.\nPublic Key (n, e): {n}, {e}\nPrivate Key (n, d): {n}, {d}")
            except Exception as ex:
                print(f"Error: {ex}")

        elif choice == '2':
            # Encrypt a message and save it
            try:
                n, e = load_public_key()
                message = input("Enter message to encrypt: ")
                ciphertext = rsa_encrypt(message, e, n)
                save_message(ciphertext)
                print("Message encrypted and saved to message.txt")
            except Exception as ex:
                print(f"Error: {ex}")

        elif choice == '3':
            # Decrypt a saved message using private key
            try:
                n, d = load_private_key()
                ciphertext = load_message()
                message = rsa_decrypt(ciphertext, d, n)
                print("Decrypted Message:", message)
            except Exception as ex:
                print(f"Error: {ex}")

        elif choice == '4':
            # Exit the program
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()