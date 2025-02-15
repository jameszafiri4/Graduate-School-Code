
# importing random module to create random vector
import random

'''
This function will create the random vector (output) that we need in this problem.
It will use the randint method to add numbers to the vector we want.
'''
def randomVector():
    # first creating empty vector
    myVector = []
    # looping through by the size of the vector we want
    for i in range(1000):
        # creating 1000 random ints between 1 and 100 so there is better chance of repeat
        n = random.randint(1, 100)
        # adding random number to vector we created
        myVector.append(n)
    # this returns the fully complete vector after loop
    return myVector

'''
This function will take an array (input) and then sort it. After this,
it will find the mode of the sortred array by using an algorithm that
is less complex than a brute force one.
'''
def findMode(a):
    # we will first sort the inputted array
    a.sort()
    # we will start with the first element being the mode
    mode = a[0]
    # our current number is the first element of the array
    curr_num = a[0]
    # setting the max count for the mode to 1 since we start at index 0
    maxCount = 1
    # our current count is being set to 1 since we already started with first
    curr_count = 1

    # now we will loop through the sorted array starting at second element
    for i in range(1, len(a)):
        # if the next element is equal to our current, increase the count
        if a[i] == curr_num:
            curr_count +=1
        # if not the same number
        else:
            # we will check if our count is bigger than max count
            if curr_count > maxCount:
                # the mode will now be the current number of count
                mode = curr_num
                # our max count will be the current count
                maxCount = curr_count
            # set the current number to element of this iteration
            curr_num = a[i]
            # reset the count for the next new number
            curr_count = 1
            
    # once we loop through, we will see if our current count is bigger
    if curr_count > maxCount:
        # update the mode to the number of this count
        mode = curr_num
    
    # we now return our mode
    return mode

'''
In our main function we will create a random array and then we
will find the mode using the function we created that more efficient
than brute force (better than O(n^2)).
'''
def main():
    a = randomVector()
    mode = findMode(a)
    print("The mode of this array is:", mode)


if __name__ == "__main__":
    main()

