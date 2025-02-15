'''
This program will create 10 random vectors; each one going from 1000 to 10,000 elements.
There will also be a sorting algorithm (quicksort) that is implemented and applied to
each of these 10 vectors. The purpose, using cProfile, is to compute the time complexitly
of the sorting algorithm and see how long it takes to sort each of the vectors
(1000, 2000, 3000... 10,000 elements) respectively.
'''

# importing random module to create random vector
import random
# importing cProfile module to see how long the sorting takes
import cProfile

'''
This function will create the random vector (output) that we need in this problem.
It will use the randint method to add numbers to the vector we want (size is input).

'''
def randomVector(size):
    # first creating empty vector
    myVector = []
    # looping through by the size of the vector we want
    for i in range(size):
        # creating a random positive/negative integer
        n = random.randint(-100000, 100000)
        # adding random number to vector we created
        myVector.append(n)
    # this returns the fully complete vector after loop
    return myVector

'''
This function will implement the quicksort algorithm. This is a recursive
sorting algorithm that works by splitting an array (input) into two sub-arrays.
There will be a pivot element, and one of the sub-arrays contains elements
smaller than that pivot, while the other contains larger elements (left & right).
The output results in a now sorted array.
'''
def quicksort(vector):
    # checks if vector has only 1 element (or zero) if so, it's already sorted
    if len(vector) <= 1:
        # returns already sorted vector
        return vector
    # the first element is used as a pivot to divide the array into two sub-arrays
    pivot = vector[0]
    # empty array for the sub-arrays, the left (smaller) and right (bigger)
    left = []
    right = []
    # loops to check the rest of the array not including pivot
    for i in vector[1:]:
        # smaller element than pivot gets added to left sub-array
        if i <= pivot:
            left.append(i)
        # if the element is bigger than the pivot it gets added to the right sub-array
        else:
            right.append(i)
    # using recursion, we will also sort the left and right arrays
    # in order, this returns the sorted left array, pivot in the middle, followed by sorted right
    return quicksort(left) + [pivot] + quicksort(right)

'''
Now we have our main function where we will create each of the 10 random vectors.
We will then use the sorting method on each one of these, and then with cProfile
be able to see how long they took to sort after the program is ran.
'''
def main():
    # here we are creating a random vector for each specified amount (increasing by 1000)
    vector_one = randomVector(1000)
    vector_two = randomVector(2000)
    vector_three = randomVector(3000)
    vector_four = randomVector(4000)
    vector_five = randomVector(5000)
    vector_six = randomVector(6000)
    vector_seven = randomVector(7000)
    vector_eight = randomVector(8000)
    vector_nine = randomVector(9000)
    vector_ten = randomVector(10000)
    # next we are going to sort each of the randomly created vectors
    sort_one = quicksort(vector_one)
    sort_two = quicksort(vector_two)
    sort_three = quicksort(vector_three)
    sort_four = quicksort(vector_four)
    sort_five = quicksort(vector_five)
    sort_six = quicksort(vector_six)
    sort_seven = quicksort(vector_seven)
    sort_eight = quicksort(vector_eight)
    sort_nine = quicksort(vector_nine)
    sort_ten = quicksort(vector_ten)

if __name__ == "__main__":
    cProfile.run("main()")
