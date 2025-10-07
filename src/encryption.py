# encryption.py
# Handles encryption and decryption of passwords using Fernet

from cryptography.fernet import Fernet
from config import ENCRYPTION_KEY

# Initialize Fernet cipher with the key from config
cipher = Fernet(ENCRYPTION_KEY)


def encrypt_password(password):
    """
    Encrypts a password using Fernet encryption

    Args:
        password (str): Plain text password to encrypt

    Returns:
        str: Encrypted password as string
    """
    encrypted = cipher.encrypt(password.encode())
    return encrypted.decode()


def decrypt_password(encrypted_password):
    """
    Decrypts an encrypted password using Fernet decryption

    Args:
        encrypted_password (str): Encrypted password string

    Returns:
        str: Decrypted plain text password
    """
    decrypted = cipher.decrypt(encrypted_password.encode())
    return decrypted.decode()
