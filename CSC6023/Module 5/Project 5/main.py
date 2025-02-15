'''
In this program we will implement a Double Array Queue and test it for
a very large case (100,000 randomly decided operations of enqueue or dequeue)

The program will compute the number of costly operations and cheap operations

The program will also ask the user about the ratio between enqueue and dequeue operations:

The probability of enqueues and dequeues should never be of less than half the other
(34% enqueues - 66% dequeues or 66% enqueues - 34% dequeues)
'''

# importing random module for operations
import random

# creating class for double array queue
class DoubleArrayQueue:
    '''
    This is our constructor method to initialize the queue by creating
    an empty array, and starting positions for the front and back.
    '''
    def __init__(self):
        self.array = []
        self.front = 0
        self.back = -1

    '''
    This method is meant to add items to the front of the queue, while
    also increasing the back position count.
    '''
    def enqueue_front(self, d):
        self.array.insert(self.front, d)
        self.back += 1

    '''
    This method is meant to add items to the back of the queue, while
    also increasing the back position count.
    '''
    def enqueue_back(self, d):
        self.array.append(d)
        self.back += 1

    '''
    This method is meant to remove items at the front of the queue, while
    also decreasing the back position count.
    '''
    def dequeue_front(self):
        if self.is_empty():
            return None
        d = self.array.pop(self.front)
        self.back -= 1
        return d

    '''
    This method is meant to remove items at the back of the queue, while
    also decreasing the back position count.
    '''
    def dequeue_back(self):
        if self.is_empty():
            return None
        d = self.array.pop()
        self.back -= 1
        return d

    '''
    This method is just meant to check if the queue is empty.
    '''
    def is_empty(self):
        return self.size() == 0

    '''
    This method is just meant to check the size of the queue.
    '''
    def size(self):
        return self.back - self.front + 1


'''
It is now time to create our main function where we will interact
with the user asking for the ratio of operations, as well as
computing the number of costly/cheap operations.
'''
def main():
    # instantiating an array object based on created class
    doubleArray = DoubleArrayQueue()
    # initializing variables we need below
    costly = 0
    cheap = 0

    # we will now create a loop to ask for the user's input
    while True:
        # exception handling for bad inputs
        try:
            ratio = float(input("Enter the ratio between enqueue & dequeue operations (must be between 0.34 and 0.66): "))
            # making sure input is within threshold
            if 0.34 <= ratio <= 0.64:
                break
            print("\nPlease try again and enter a valid ratio.\n")
        # incase input is not a number
        except ValueError:
            print("\nPlease try again and enter a valid number for the ratio.\n")

    # we will now create a loop to perform operations on the queue
    for i in range(100000):
        ops = random.random()
        # if less than given ratio, add to front which is cheap
        if ops <= ratio:
            doubleArray.enqueue_front(i)
            cheap += 1
        # if greater than or equal to given ratio
        else:
            # if array is empty, add data to front which is costly
            if doubleArray.is_empty():
                doubleArray.enqueue_front(i)
                costly += 1
            # if array is not empty, remove from the back which is cheap
            else:
                doubleArray.dequeue_back()
                cheap += 1

    # we will now print the results to the user
    print("\nFinal size of the queue:", doubleArray.size())
    print("Number of costly operations:", costly)
    print("Number of cheap operations:", cheap)
    print("Percentage of costly operations:", (costly/100000) * 100, "%")
    print("Percentage of cheap operations:", (cheap/100000) * 100, "%")
    

if __name__ == "__main__":
    main()
