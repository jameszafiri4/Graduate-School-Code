'''
- This program will create a random list and a copy of that list
- It will then test the merge and insertion sorting methods on them
- It will show the speed of the methods using timestamps
'''

# importing modules to use timestamps and make random list
import time
import random
from datetime import datetime

# importing sorting methods from downloaded class examples
from mergeSort import merge_sort
from insertionSort import insertion_sort

# creating variable for the size of the list
listSize = 20000
# creating an empty list
myList = []

# loop to add random numbers to the empty list
for i in range(0, listSize):
    n = random.randint(1, 25000)
    myList.append(n)
print("There are", len(myList), "items in the list we are going to sort.")

# making a copy of the list to use in test
yourList = myList.copy()

# starting timer running method then ending the time
start = time.time()
merge_sort(myList)
end = time.time()
print("The time taken to run the merge sort method is: ", end - start, "seconds")

# starting timer running next method with copied list then ending the time
start = time.time()
insertion_sort(yourList)
end = time.time()
print("The time taken to run the insertion sort method is: ", end - start, "seconds")
