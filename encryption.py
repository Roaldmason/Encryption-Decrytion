
from cryptography.fernet import Fernet

# Generate a key (store it safely; anyone with it can decrypt)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(text: str) -> bytes:
    return cipher.encrypt(text.encode())

def decrypt(token: bytes) -> str:
    return cipher.decrypt(token).decode()

message = "Hello, this is a secret!"
encrypted = encrypt(message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted))