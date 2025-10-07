# database.py
# Handles database connection and table creation

import mysql.connector
from config import DB_CONFIG

def get_connection():
    # Establishes connection to MySQL server (without specifying database)
    # Returns connection object
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def get_db_connection():
    # Establishes connection to the password_manager_db database
    # Returns connection object
    
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def setup_database():

    # Creates database and tables if they don't exist
    # - Creates password_manager_db database
    # - Creates users table (id, username, password)
    # - Creates passwords table (id, user_id, website, username, password)

    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS password_manager_db")
        print("Database 'password_manager_db' ready.")
        
        cursor.close()
        connection.close()
    
    # Now connect to the database and create tables
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL
            )
        """)
        
        # Create passwords table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                website VARCHAR(200) NOT NULL,
                username VARCHAR(100) NOT NULL,
                password TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)
        
        connection.commit()
        print("Tables created successfully.")
        
        cursor.close()
        connection.close()