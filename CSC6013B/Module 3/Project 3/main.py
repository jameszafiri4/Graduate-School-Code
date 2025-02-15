'''
This is the main function where we will first read the text file containing
the numbers, and then create an array of those numbers stored as integers
We will then store those numbers into a binary tree so we can print out the
graph we want as a matrix using the class methods
'''

from binaryTree import BinaryTree

def readText():
    '''
    This is the method we are going to use to read
    the numbers from the text file and then store
    them into an empty array
    '''
    numbers = []
    text = open("numbers.txt", "r")
    for i in text:
        numbers.append(int(i))
    return numbers

def main():
    '''
    This is our main method where we will store the array
    we created as a binary tree from the class we imported
    We will then print out a matrix based off a graph of the
    new tree of our numbers we made, looking at each row
    '''
    nums = readText()

    tree = BinaryTree(nums)
    for i in nums:
        tree.insert(int(i))

    tree.printMatrix()


if __name__ == "__main__":
    main()
