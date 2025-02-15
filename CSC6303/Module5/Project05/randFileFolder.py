'''
Simple program that creates a folder and saves a file with
100 random numbers between 0-1000 inside of it.
The program checks to see if the folder name given exists
using the os module that is being imported.
This code is written in Python and was tested on Visual Studio Code.
James Zafiri
version 1.0.0
Week 5 of CSC6303
'''

import os
import random

'''
This function is meant to check if the folder exists, and then
remove/create the folder depending on that.
'''
def create_folder(folder_name):
    # first checking if the folder exists
    if os.path.exists(folder_name):
        # if the folder does exist, remove it
        os.system(f"rm -r '{folder_name}'")

    # creating the folder if it doesn't already exist/after removing it
    os.makedirs(folder_name)

'''
This function is meant to generate 100 random numbers, and then
create a text file to save these numbers to in the given folder.
'''
def save_random_numbers(folder_name):
    # generating 100 random numbers between 0 and 1000
    random_numbers = [random.randint(0, 1000) for n in range(100)]
    # creating and saving the random numbers to a file in the folder
    with open(os.path.join(folder_name, "numbers100.txt"), "w") as file:
        for number in random_numbers:
            file.write(str(number) + "\n")

'''
This is our main function where we will interact with the user and
ask them for a folder name to call our functions and create the folder
with the file of random numbers inside of it.
'''
def main():
    # asking the user for the folder name
    folder_name = input("Enter the name of the folder you want to create: ")

    # checking if folder exists/creating the folder using prior function 
    create_folder(folder_name)
    # creating file of the random numbers to save in the folder
    save_random_numbers(folder_name)

    print("The folder and file were both created successfully.")

if __name__ == "__main__":
    main()
