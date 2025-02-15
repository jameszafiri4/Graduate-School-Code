'''
- On this program we will be able to read a list of integers that are taken from a text file
- The file will include 16 numbers, which will be stored into an array and then sorted
- This sorted array will then be stored into a LinkedList structure that is an imported class
- We will ask the user for an integer, and look for a position to store it in the linked list
- If that value is already included in the list, we will remove it
- If not, we will insert it appropriately so the list remains sorted
'''

from LinkedList import Node, LinkedList

def dataStorage():
    '''
    This function will read the data text file and create an array that will store the numbers
    This array containing the numbers of the file will then be sorted
    '''
    a = []
    data = open("data.txt", "r")
    for i in data:
        a.append(int(i))
    a.sort()
    return a
    
def main():
    '''
    This is the main function where we take the sorted list and then store it into a linked list
    We will use the LinkedList class to perform the functions of a linked list
    This is where we will loop through and ask the user to enter an integer to add to the list
    '''
    # calling the function to create the sorted array
    a = dataStorage()
    # instantiating an object of LinkedList class to store sorted array into a linked list
    L = LinkedList()
    # this will loop through the sorted array and add the numbers to the linked list
    for i in reversed(a):
        L.insertBeginning(i)

    # this will print out the list to show the user
    L.printList()
    print("This is the current list.")
        
    # this is meant to loop through and ask the user for integers using exception handling
    while True:
        try:
            x = int(input("\nPlease enter an integer to add: "))
            break
        except ValueError:
            print("Please enter a valid integer.\n")

    for i in a:
        '''
        This is looking at the numbers we passed through from the data file
        It will evaluate the current and next nodes using LinkedList class methods
        If the user's integer is already in the list it will be removed
        If not, it will be added and keep the correct order of the linked list
        '''
        L.nextCurrent()
        currentData = L.Current.Data
        # exception handling if value is None
        try:
            nextData = L.Current.Next.Data
        except:
            nextData = None
        # removes integer user entered if it is in the list already    
        if x == nextData:
            print(f"\n{x} is already in the linked list. Now removing {x}.\n")
            L.removeCurrentNext()
            break
        # removes integer user entered if it is the first in the list
        elif x == a[0]:
            print(f"\n{x} is already in the linked list. Now removing {x}.\n")
            L.removeBeginning()
            break
        # inserts user's integer at the beginning if it smaller than all the values in the list
        elif x < a[0]:
            print(f"\n{x} was not found in the linked list.")
            print(f"Now adding {x} at the beginning of the list.\n")
            L.insertBeginning(x)
            break
            '''
            This is meant to add the user's integer if it is greater than the current, but also
            less than the next number. It will get added to the correct spot inbetween.
            However, if the next value is none (end of list), we use the LinkedList method
            to add the number to the end of the list
            '''
        elif x > currentData and (x < nextData if nextData is not None else L.insertEnd(x)):
            if nextData is not None:
                print(f"\n{x} was not found in the linked list.")
                print(f"Now adding {x} between {currentData} and {nextData}.\n")
                L.insertCurrentNext(x)
                break
        # prints message for user if the number was added to the end of the list (based off above)
        elif x > currentData and nextData is None:
            print(f"\n{x} was not found in the linked list.")
            print(f"Now adding {x} at the end of the list.\n")
            break

    # prints updated list for the user
    L.printList()
    print("This is now the updated list.")

if __name__ == "__main__":
    main()
