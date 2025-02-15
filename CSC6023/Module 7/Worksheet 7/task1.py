'''
This program will generate a random array of 10,000 elements with an equal number
of 0s and 1s and then will implement the randomized Las Vegas algorithm that
searches for an element holding a 1.

The program will then output the position of the first 1 found, plus the number
of tries before finding it.
'''
import random

'''
In this function we will create the random array of 0s and 1s. We will
first add 5000 of each to an array. After that we will shuffle it using the
random module we imported, which results of an output of the array we want.
'''
def randArray():
    # this will make a list containing 5000 0s and 5000 1s
    vegas = ([0] * 5000) + ([1] * 5000)
    # we will now use the random shuffle method on the array
    random.shuffle(vegas)
    return vegas

'''
In this function we will actually implement the Las Vegas algorithm.
We will randomly search through an inputted array until a 1 is found.
We will then return the index of where the first 1 is found and how many
tries it took before finding the 1.
'''
def lasVegasAlg(A):
    # count for the tries it takes
    tries = 0
    while True:
        # each iteration is a try
        tries += 1
        # now to pick a random spot of the array
        position = random.randint(0, len(A) - 1)
        # checking if the spot is a 1
        if A[position] == 1:
            return position,tries
'''
This is our main function where we will implement the above functions
and test out the Las Vegas algorithm on the randomized array of 0s and 1s.
We will output the position of the first 1 found as well as the number of tries.
'''
def main():
    # creating an array of 5000 0s and 5000 1s then randomly shuffling it
    a = randArray()
    # implementing randomized Las Vegas algorithm on created array
    output = lasVegasAlg(a)

    # we will now print out the results for the user
    print(f"A '1' was found at position {output[0]} of the array after {output[1]} tries.")


if __name__ == "__main__":
    main()
