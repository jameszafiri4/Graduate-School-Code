'''
This program will create a completely random vector of 1000 positive and negative integers.
It will then find the maximum contiguous subsequence sum value and print it out.

Extends Task 1 to not only print out the max sum value, but we will also print out the
initial and final index of the elements used to compute the max sum that was found.
'''

# importing random module to create random vector
import random

'''
This function will create the random vector that we need in this problem.
It will use the randint method to add numbers to the vector we want.
'''
def randomVector(size):
    # first creating empty vector
    myVector = []
    # looping through by the size of the vector we want
    for i in range(size):
        # creating a random positive/negative integer
        n = random.randint(-100, 100)
        # adding random number to vector we created
        myVector.append(n)
    # this returns the fully complete vector after loop
    return myVector

'''
This function will find the maximum contiguous subsequence of the vector we created.
It will use a loop to compare sums as it goes through the array. This uses the example
from class so the time complexity is O(n) (linear) and more efficient. In this task it
will now also print out the initial and final elements used to compute the max sum.
'''
def maxSubsequence(vector):
    # setting our max sum as zero to begin
    max_sum = 0
    # also setting current sum to zero at first
    curr_sum = 0
    # setting initial element to zero
    start = 0
    # setting final element to zero
    final = 0

    # looping through the entire random vector created
    for i in range(len(vector)):
        # adds element of vector to the current sum
        curr_sum += vector[i]
        # if current sum is greater than max sum
        if (curr_sum > max_sum):
            # current sum will become new max sum
            max_sum = curr_sum
            # last element used when max sum is found
            final = vector[i]
        # otherwise if the current sum was negative
        elif (curr_sum < 0):
            # this keeps track of the start of the subsequence (element after negative found)
            start = vector[i + 1]
            # current sum will be set back to zero
            curr_sum = 0
    # after loop this returns the maximum sum, initial and final elements
    return max_sum, start, final

# main function to create random vector and find max sum when program is ran
def main():
    # calling randomVector function to create one based on 1000 integers
    randVector = randomVector(1000)
    # calling maxSubsequence function to find max sum of random vector that was created
    max_sub_sum = maxSubsequence(randVector)
    # prints out the value of the max sub sum that we found, as well as first and last elements
    print(f"The maximum subsequence sum and its first and last elements are: {max_sub_sum}")

if __name__ == "__main__":
    main()
