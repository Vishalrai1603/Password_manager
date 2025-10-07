# password_manager.py
# Main application file - CLI Password Manager

from database import setup_database
from user_operations import signup, login
from password_operations import add_password, view_passwords, search_password, delete_password

def main_menu():
    #Displays the main menu before login. Handles Signup, Login, and Exit options
    print("\n" + "="*40)
    print("     PASSWORD MANAGER")
    print("="*40)
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    print("="*40)

def user_menu():
    # Displays the menu after user login.Handles password management operations
    print("\n" + "="*40)
    print("     PASSWORD MANAGEMENT")
    print("="*40)
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Logout")
    print("="*40)

def main():
    #Main function that runs the password manager application

    setup_database()
    
    current_user_id = None
    
    while True:
        if current_user_id is None:
            # Show main menu if not logged in
            main_menu()
            choice = input("\nEnter your choice: ")
            
            if choice == '1':
                # Signup
                print("\n--- SIGNUP ---")
                username = input("Enter username: ")
                password = input("Enter password: ")
                signup(username, password)
                
            elif choice == '2':
                # Login
                print("\n--- LOGIN ---")
                username = input("Enter username: ")
                password = input("Enter password: ")
                user_id = login(username, password)
                if user_id:
                    current_user_id = user_id
                    
            elif choice == '3':
                # Exit
                print("\nThank you for using Password Manager. Goodbye!")
                break
                
            else:
                print("\nInvalid choice. Please try again.")
        
        else:
            # Show user menu if logged in
            user_menu()
            choice = input("\nEnter your choice: ")
            
            if choice == '1':
                # Add Password
                print("\n--- ADD PASSWORD ---")
                website = input("Enter website/app name: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                add_password(current_user_id, website, username, password)
                
            elif choice == '2':
                # View Passwords
                view_passwords(current_user_id)
                
            elif choice == '3':
                # Search Password
                print("\n--- SEARCH PASSWORD ---")
                website = input("Enter website/app name to search: ")
                search_password(current_user_id, website)
                
            elif choice == '4':
                # Delete Password
                print("\n--- DELETE PASSWORD ---")
                password_id = input("Enter password ID to delete: ")
                try:
                    password_id = int(password_id)
                    delete_password(current_user_id, password_id)
                except ValueError:
                    print("\nInvalid ID. Please enter a number.")
                    
            elif choice == '5':
                # Logout
                print("\nLogged out successfully!")
                current_user_id = None
                
            else:
                print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()