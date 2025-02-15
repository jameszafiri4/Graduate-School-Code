'''
Simple program that discovers the current OS and asks the
user a file name with path and converts it according to system.
This code is written in Python and was tested on Visual Studio Code.
James Zafiri
version 1.0.0
Week 6 of CSC6303
'''

import platform
import os

'''
This is the function where the file path conversion is done.
It checks the current OS of the user, and will correct the file
path entered by them based on their system.
'''
def convert_file_path(file_path):
    if platform.system() == 'Windows':
        return file_path.replace('/', '\\')
    else:
        return file_path.replace('\\', '/')

'''
This is the main function where we will be interacting with the user.
We will first display their current operating system and then ask
them to enter a file path. It will then be converted or they will be
told it is already in the correct format.
'''
def main():
    print("Name of the current operating system:", os.name)
    print("\nName of the current OS system:", platform.system())
    user_file_path = input("\nEnter the file name with path: ")

    converted_path = convert_file_path(user_file_path)
    if converted_path == user_file_path:
        print("\nThe entered file path is already in the format expected by the current operating system.")
    else:
        print("\nThe file path has been converted according to the system:", converted_path)

if __name__ == "__main__":
    main()
