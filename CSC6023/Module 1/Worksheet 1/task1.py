'''
This program will create a completely random vector of 1000 positive and negative integers.
It will then find the maximum contiguous subsequence sum value and print it out.
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
from class so the time complexity is O(n) (linear) and more efficient.
'''
def maxSubsequence(vector):
    # setting our max sum as zero to begin
    max_sum = 0
    # also setting current sum to zero at first
    curr_sum = 0

    # looping through the entire random vector created
    for i in range(len(vector)):
        # adds element of vector to the current sum
        curr_sum += vector[i]
        # if current sum is greater than max sum
        if (curr_sum > max_sum):
            # current sum will become new max sum
            max_sum = curr_sum
        # otherwise if the current sum was negative
        elif (curr_sum < 0):
            # current sum will be set back to zero
            curr_sum = 0
    # after loop returns the maximum sum
    return max_sum

# main function to create random vector and find max sum when program is ran
def main():
    # calling randomVector function to create one based on 1000 integers
    randVector = randomVector(1000)
    # calling maxSubsequence function to find max sum of random vector that was created
    max_sub_sum = maxSubsequence(randVector)
    # prints out the value of the max sub sum that we found
    print(f"The maximum subsequence sum is: {max_sub_sum}")

if __name__ == "__main__":
    main()
