# Basic-File-Handler

# File Read & Write Challenge 🖋️  

This Python script reads a file, modifies its content, and writes the modified content to a new file. It includes error handling to manage issues such as missing files or permission errors. I have submitted this as part of my assignment for the Python module; for the PLP Programme. 

## Features  
✅ Reads a file provided by the user  
✅ Converts the content to uppercase (modification step)  
✅ Writes the modified content to a new file  
✅ Handles errors gracefully (file not found, permission errors, etc.)  
✅ Ensures files are closed properly using `finally`  

## How to Use  
1. **Run the script:**  
   ```sh
   python modify_file.py
   ```
2. Enter the filename when prompted.
3. If the file exists, a new file with the modified content will be created (modified_filename).
4. If the file does not exist, an error message will be displayed.