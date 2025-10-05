from password_manager import add_password, get_password

while True:
    print("\nPassword Manager")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        website = input("Enter website name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        add_password(website, username, password)

    elif choice == "2":
        website = input("Enter website name: ")
        username = input("Enter username: ")
        password = get_password(website, username)
        if password:
            print(f"Password for {website} ({username}): {password}")
        else:
            print("No credentials found!")
    
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")
