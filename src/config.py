# config.py
# Configuration file for storing encryption key

# Fixed Fernet encryption key (DO NOT CHANGE - all passwords encrypted with this key)
# In a real application, this should be stored securely, not in code
ENCRYPTION_KEY = b'8cozhW7kKsLZPkGXgJHvCAkPaAMdIQQ3kZpZq7RGZMA='

# MySQL Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',          # Change to your MySQL username
    'password': '12345',          # Change to your MySQL password
    'database': 'password_manager_db'
}
