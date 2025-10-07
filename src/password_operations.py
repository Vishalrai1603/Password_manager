# password_operations.py
# Handles all password-related operations (Add, View, Search, Delete)
import mysql.connector
from database import get_db_connection
from encryption import encrypt_password, decrypt_password


def add_password(user_id, website, username, password):
    # Adds a new password entry for the user
    # Encrypts the password before storing in database

    # Args:
    #     user_id (int): ID of the logged-in user
    #     website (str): Website or app name
    #     username (str): Username for the website
    #     password (str): Password to encrypt and store

    # Returns:
    #     bool: True if password added successfully, False otherwise
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()

        # Encrypt password before storing
        encrypted_pwd = encrypt_password(password)

        try:
            cursor.execute(
                "INSERT INTO passwords (user_id, website, username, password) VALUES (%s, %s, %s, %s)",
                (user_id, website, username, encrypted_pwd)
            )
            connection.commit()
            print("\nPassword added successfully!")
            cursor.close()
            connection.close()
            return True
        except mysql.connector.Error as err:
            print(f"\nError adding password: {err}")
            cursor.close()
            connection.close()
            return False
    return False


def view_passwords(user_id):
    # Displays all saved passwords for the logged-in user
    # Decrypts passwords before displaying

    # Args:
    #     user_id (int): ID of the logged-in user
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()

        # Fetch all passwords for the user
        cursor.execute(
            "SELECT id, website, username, password FROM passwords WHERE user_id = %s",
            (user_id,)
        )
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        if results:
            print("\n" + "="*60)
            print("YOUR SAVED PASSWORDS")
            print("="*60)
            for row in results:
                pwd_id, website, username, encrypted_pwd = row
                # Decrypt password for display
                decrypted_pwd = decrypt_password(encrypted_pwd)
                print(f"\nID: {pwd_id}")
                print(f"Website: {website}")
                print(f"Username: {username}")
                print(f"Password: {decrypted_pwd}")
                print("-"*60)
        else:
            print("\nNo passwords saved yet.")


def search_password(user_id, website):
    # Searches for passwords by website name

    # Args:
    #     user_id (int): ID of the logged-in user
    #     website (str): Website name to search for
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()

        # Search for passwords matching the website name
        cursor.execute(
            "SELECT id, website, username, password FROM passwords WHERE user_id = %s AND website LIKE %s",
            (user_id, f"%{website}%")
        )
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        if results:
            print("\n" + "="*60)
            print(f"SEARCH RESULTS FOR: {website}")
            print("="*60)
            for row in results:
                pwd_id, website, username, encrypted_pwd = row
                # Decrypt password for display
                decrypted_pwd = decrypt_password(encrypted_pwd)
                print(f"\nID: {pwd_id}")
                print(f"Website: {website}")
                print(f"Username: {username}")
                print(f"Password: {decrypted_pwd}")
                print("-"*60)
        else:
            print(f"\nNo passwords found for '{website}'.")


def delete_password(user_id, password_id):

    # Deletes a password entry by its ID

    # Args:
    #     user_id (int): ID of the logged-in user
    #     password_id (int): ID of the password entry to delete

    # Returns:
    #     bool: True if deleted successfully, False otherwise
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()

        try:
            # Delete password entry (ensure it belongs to the user)
            cursor.execute(
                "DELETE FROM passwords WHERE id = %s AND user_id = %s",
                (password_id, user_id)
            )
            connection.commit()

            if cursor.rowcount > 0:
                print("\nPassword deleted successfully!")
                cursor.close()
                connection.close()
                return True
            else:
                print("\nPassword not found or you don't have permission to delete it.")
                cursor.close()
                connection.close()
                return False
        except mysql.connector.Error as err:
            print(f"\nError deleting password: {err}")
            cursor.close()
            connection.close()
            return False
    return False
