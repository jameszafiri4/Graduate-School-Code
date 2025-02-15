'''
In this program we will call the function "myFunction(x)" from 0 to 9999 and apply the
Hill Climbing algorithm to find the value of x that delivers the largest value for the function.

We will implement a version where the initial search value x is chosen randomly between the values 1 to 9998.

We will use the myFunction implementation given to us in class. There will also be a function
included called "hillClimb(arr, start_index)" that will return the index of the local peak and
the value in this fashion: return local_maximum_index, arr[local_maximum_index].

If the starting index is a local peak, the starting index and its value should be returned.
If the starting index ends up in a pit, with equal increases to the left and to the right, search to the right.
If the starting index ends up in a pit with unequal increases to the left and right, search the higher path.

We will make sure the searching can go all the way to the ends of the array if need be.
We will make sure the program can traverse shoulders. If at the end of the shoulder, the values start to decrease,
we should end at the last part of the shoulder. For example hillClimb([6,5,5,5,4,3,2],5) should return
the index 0 and the value 6 but hillClimb([2,5,5,5,4,3,2],5) should return the index 1 and the value 5.
'''
# we will use the math module to make the calculations needed
from math import log2
# using the random module to generate random starting index
import random

'''
This function is what was given to us in class. It will be used to create an array, taking an
input x which will be an integer paramter for the initial search value. The output results in
the initial best value.
'''
def myFunction(x):
    if (x == 0):
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x))**3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x)*2)**3
    else:
        return (log2(x)**2) - x

'''
This function takes two inputs: an array (arr), and a starting index (start_index). The array will later
be generated using myFunction above, and the starting index will be generated using the random module
in Python. The output will be the index of the local peak, as well as the value of the local maximum
according to the specifications of the prompt that are listed.
'''
def hillClimb(arr, start_index):
    # setting max values place holders as negative infinity (not zero incase list has negative numbers)
    local_maximum_index = float("-inf")
    local_maximum_value = float("-inf")
    # looping throught the array, skipping by 3 since we look at the left and right values too
    for x in range(0, len(arr) - 1, 3):
        # place holder for current value of array
        value = arr[x]
        # looking at neighbor values of x
        for n in [x-1, x+1]:
            # giving neighbor value a variable
            n_value = arr[n]
            # here is where we will compare and update as necessary (if curr/neighbor value is bigger than best)
            if n_value > local_maximum_value or value > local_maximum_value:
                # if neighboring value is bigger, make it best value
                if n_value > value:
                    local_maximum_value = n_value
                # or the best value stays at current value
                else:
                    local_maximum_value = value
                # here we are updating the best index, same principle as above
                if n_value > value:
                    local_maximum_index = n
                else:
                    local_maximum_index = x
    return local_maximum_index, local_maximum_value


'''
This is our main function where we will use the above functions to complete our task. First,
we will create an array using the "myFunction" function based on size constraint given. Next,
we will create a random starting index based on size constraint given. Lastly, we will enter
both of these values into the "hillClimb" function to get the output we want to print to the user.
'''
def main():
    # we will first create the array we want using function from above from range 0 to 9999
    arr = [myFunction(x) for x in range(0, 9999)]
    # we will now create our starting index, random number from 1 - 9998
    start_index = random.randint(1, 9998)

    # variable to return the maximum index and value
    local_max = hillClimb(arr, start_index)

    print("The local maximum index is:", local_max[0])
    print("The local maximum value is:", local_max[1])


if __name__ == "__main__":
    main()
