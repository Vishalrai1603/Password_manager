# config.py
# Configuration file for storing encryption key

# Fixed Fernet encryption key (DO NOT CHANGE - all passwords encrypted with this key)

ENCRYPTION_KEY = b'8cozhW7kKsLZPkGXgJHvCAkPaAMdIQQ3kZpZq7RGZMA='

# MySQL Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',          
    'password': '12345',          
    'database': 'password_manager_db'
}
