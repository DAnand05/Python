while True:
    choice = input("Do you want to create a new file? (Enter 'create' or 'exit'): ")
    if choice == "create":
            file_name=input("Enter the file name: ")
            # Ask the user for their information
            name = input("Enter your name: ")
            father_name = input("Enter your father's name: ")
            mother_name = input("Enter your mother's name: ")
            address = input("Enter your address: ")
            phone_number = input("Enter your phone number: ")

            # Open a file called "user_info.txt" in write mode
            with open(file_name, "w") as f:
                # Write the user's information to the file
                f.write(f"Name: {name}\n")
                f.write(f"Father's Name: {father_name}\n")
                f.write(f"Mother's Name: {mother_name}\n")
                f.write(f"Address: {address}\n")
                f.write(f"Phone Number: {phone_number}\n")

            # Let the user know the information has been written to the file
            print(f"Your information has been written to {file_name}.")
    elif choice == "exit":
            break
    else:
            print("Invalid choice. Please enter 'create' or 'exit'.")