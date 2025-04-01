def modify_file():
    filename = input("Enter the filename to read: ")

    try:
        file = open(filename, "r")
        content = file.read()
        modified_content = content.upper()
        new_filename = "modified_" + filename
        new_file = open(new_filename, "w")
        new_file.write(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    
    except PermissionError:
        print("Error: You don't have permission to read the file.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        try:
            file.close()
        except NameError:
            pass
        try:
            new_file.close()
        except NameError:
            pass

modify_file()
