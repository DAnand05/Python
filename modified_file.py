import os

# Function to search for a specific string in the file
def search_file(file_name, string_to_search):
    with open(file_name, "r") as f:
        for line in f:
            if string_to_search in line:
                print(f"'{string_to_search}' found in {file_name}")
                return True
    print(f"'{string_to_search}' not found in {file_name}")
    return False

# Function to delete a specific line from the file
def delete_line(file_name, string_to_search):
    if search_file(file_name, string_to_search):
        os.remove(file_name)
        print(f"{file_name} deleted as '{string_to_search}' was found in the file")




# Ask the user if they want to search or delete information from the file
while True:
    choice = input("Do you want to search or delete information from the file? (Enter 'search', 'delete', or 'exit'): ")
    if choice == "search":
        # Ask the user for the string to search for
        search_string = input("Enter the string to search for: ")
        file_name = input("Enter file name: ")
        # Call the search_file function to search for the string in the file
        search_file(file_name, search_string)
    elif choice == "delete":
        # Ask the user for the line to delete
        string_to_search = input("Enter the string to search: ")
        file_name = input("Enter file name: ")
        # Call the delete_line function to delete the line from the file
        delete_line(file_name, string_to_search)
    elif choice == "exit":
        break
    else:
        print("Invalid choice. Please enter 'search', 'delete', or 'exit'.")
