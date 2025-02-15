'''
This program will use an imported Stack class, an imported Person class, and the csv module
It will read a list of people from a csv and store them into a stack, each person being an
object of the Person class

The user will repeatedly be asked to enter integers from 1-4, and that amount of people
will then be popped from the stack

The program will then let the user know who is up next at the top of the stack, up until
the stack is empty which is when the program will then end

'''

import csv
from Stack import Stack
from Person import Person

def main():
    '''
    This is the main loop of the program to interact with the user
    It will first read the csv file, and use each row as a new
    Person object. It will then add these objects to the Stack

    It will make sure that the user enters a valid int 1-4 using
    exception handling
    
    '''
    # instantiate stack object
    newStack = Stack()
    # reading the csv file
    file = open("people.csv", "r")
    # using method from cvs module for efficient array creation
    read = csv.reader(file)
    # looping through the read rows of people
    # assigns each one attributes from Person class
    for i in read:
        newPerson = Person(i[0], i[1], i[2])
        newStack.push(newPerson)
    # loops as long as stack is not empty
    while not newStack.IsEmpty():
        try:
            # exception handling so user enters valid numbers
            num = int(input("Please enter a number from 1 to 4: "))
            if num < 1 or num > 4:
                print("Invalid input. Enter a number between 1 and 4\n")
                continue
            # loops through stack based on input and pops the people
            for i in range(num):
                if newStack.IsEmpty():
                    break
                newStack.pop()
            # informs the user who is up next in the stack (top person)
            if not newStack.IsEmpty():
                print("The next person on the stack is:", newStack.top().name, "\n")
            # lets user know the stack is empty
            else:
                print("The stack is empty... Goodbye!")

        except ValueError:
            print("Please enter a valid integer.\n")


if __name__ == "__main__":
    main()
