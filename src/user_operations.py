import mysql.connector
from database import get_db_connection


def signup(username, password):
    """
    Creates a new user account

    Args:
        username (str): Username for new account
        password (str): Password for new account (stored as plain text)

    Returns:
        bool: True if signup successful, False otherwise
    """
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()

        try:
            # Insert new user into database
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                           (username, password))
            connection.commit()
            print(f"\nSignup successful! Welcome, {username}!")
            cursor.close()
            connection.close()
            return True
        except mysql.connector.Error as err:
            print(f"\nError: Username '{username}' already exists or invalid.")
            cursor.close()
            connection.close()
            return False
    return False


def login(username, password):
    """
    Authenticates user and logs them in

    Args:
        username (str): Username to login
        password (str): Password to verify

    Returns:
        int or None: User ID if login successful, None otherwise
    """
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()

        # Check if username and password match
        cursor.execute(
            "SELECT id, password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result and result[1] == password:
            print(f"\nLogin successful! Welcome back, {username}!")
            return result[0]  # Return user ID
        else:
            print("\nInvalid username or password.")
            return None
    return None
