'''
In this program we will use the AVLTree implementation seen in class to ask
the user for numbers to store in an AVLTree. We have added one additional
method to the class that is meant to search the tree. If the number is in it,
it will be deleted. If not, then it will be inserted. After each action, the
tree will be printed out for the user to see. The program will keep running
after each number the user enters until that number is a negative integer.
'''

# importing the AVLTree class to create a tree based off of that
from avl import AVLTree

'''
This is our main function where we will ask the user to input integers and
call methods from the AVLTree class to perform what we need for this project.
'''
def main():
    # instantiating a tree object based on the class
    tree = AVLTree()
    # setting the root value to be None to start
    root = None

    # now we will run our loop that allows the user to keep entering numbers
    while True:
        # using exception handling in case the user enters an invalid num/char
        try:
            x = int(input("Please enter a positive integer to add to the tree (enter negative to exit): "))
            # this will exit the program if user enters negative int
            if x < 0:
                break
            # now we implement our search method to look for what the user enters
            if tree.searchTree(root, x):
                # this will delete the integer from the tree if found
                root = tree.delete_node(root, x)
                print(f"\n{x} was found in the tree and is now being removed.")
            # if the integer entered was not found it will be inserted
            else:
                root = tree.insert_node(root, x)
                print(f"\n{x} was not found in the tree and is now being added.")

            # this will print the tree after each insertion/deletion
            print("\n")
            tree.printHelper(root, "", True)
            print("\n")

        except ValueError:
            print("\nPlease enter a valid integer.\n")


if __name__ == "__main__":
    main()

