import math
import random


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def generate_keys():
    p = generate_prime()
    q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)

    return ((n, e), (n, d))


def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message


def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message


def main():
    print("RSA Cryptosystem")
    public_key, private_key = generate_keys()

    message = input("Enter the message you want to encrypt: ")
    print(f"\nYour message: {message}")

    encrypted_message = encrypt(message, public_key)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
