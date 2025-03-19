# Importing the os module to check if the file exists
import os

# Function to read a file and write a modified version to a new file
def read_and_write_file(file_name):
    # Checking if the file exists
    if os.path.exists(file_name):
        # Opening the file in read mode
        with open(file_name, 'r') as file:
            # Reading the contents of the file
            content = file.read()
        
        # Modifying the content of the file
        modified_content = content.upper()
        
        # Creating a new file to write the modified content
        new_file_name = 'modified_' + file_name
        
        # Writing the modified content to the new file
        with open(new_file_name, 'w') as new_file:
            new_file.write(modified_content)
        
        print("File read and modified successfully. New file created with name:", new_file_name)
    else:
        print("File does not exist. Please enter a valid file name.")

# Asking the user for the filename
file_name = input("Enter the filename: ")

# Calling the function to read the file and write a modified version to a new file
read_and_write_file(file_name)