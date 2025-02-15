'''
- This is a program meant to implement a dequeue in Python. It uses a Dequeue class that contains all of the methods
- The program will prompt the user to enter items to store in a list of their choosing (any items they want)
- It will then ask the user to enter an item at either the beginning or end of the queue, and will display the correct dequeue
'''

# class for the dequeue
class Dequeue:
    # constructor taking no parameters; initializes an empty list for an object
    def __init__(self):
        self.items = []
    # method to add item to beginning of the list    
    def insertFront(self, item):
        self.items.insert(0, item)
    # method to add item to end of the list
    def insertRear(self, item):
        self.items.append(item)
    # method to display the list
    def display(self):
        print(self.items)

# main function to create dequeue for user
def main():
    # creating empty string to use in loop
    userList = ""
    # creating object using Dequeue class; empty list
    emptyList = Dequeue()
    # as long as the user's input is not STOP
    while userList != "STOP":
        # prompt user to enter items
        userList = input("Please enter items you want to add to a list. Type 'STOP' to finish your list: ")
        # adds the user's inputs to the empty list; makes sure STOP doesn't get added
        if userList != "STOP":
            emptyList.insertRear(userList)
        # ends loop once user types STOP
        else:
            break
    # new line for spacing
    print("")
    # displays the user created list using method from Dequeue class
    emptyList.display()
    # asks the user to enter a new item to the list and stores it in variable
    userItem = input("\nNow enter a item you want to add to your list: ")
    # asks the user whether they want it at the front or back of the list
    front_or_back = input("\nDo you want to add this item to the front or back of the list? Type 'FRONT' or 'BACK' ")
    # checks to see if user wants the new item in the front
    if front_or_back == "FRONT":
        # if FRONT, adds to beginning of list
        emptyList.insertFront(userItem)
        print("")
        # displays the new list for the user by calling method from the class
        emptyList.display()
        print("\nThat is now your list after adding the item.")
    # checks to see if user wants the new item in the back
    elif front_or_back == "BACK":
        # if BACK, adds to end of list
        emptyList.insertRear(userItem)
        print("")
        # displays the new list for the user by calling method from the class
        emptyList.display()
        print("\nThat is now your list after adding the item.")
    # if user enters something other than FRONT or BACK, lets them know it is invalid    
    else:
        print("\nPlease run again and enter a valid command.")

# calling main function
if __name__ == "__main__":
    main()
