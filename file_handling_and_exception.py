def read_and_modify_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nOriginal file content successfully read.")
        modified_content = content.upper()  # Convert content to uppercase
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"\nModified content written to '{new_filename}'.")
    except FileNotFoundError:
        print(f"\n❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"\n❌ Error: Unable to read the file '{filename}'.")

read_and_modify_file()  # Run the function

