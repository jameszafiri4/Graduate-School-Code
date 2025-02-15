'''
This program will generate a random array of 10,000 elements with an equal number
of 0s and 1s and then will implement the randomized Monte Carlo algorithm that
searches for an element holding a 1.

k will be set to 10 (number of attempts)

The program will then output the position of the first 1 found, plus the number
of tries before finding it or a message stating that it did not find the 1 after k attempts.
'''
import random

'''
In this function we will create the random array of 0s and 1s. We will
first add 5000 of each to an array. After that we will shuffle it using the
random module we imported, which results in an output of the array we want.
'''
def randArray():
    # this will make a list containing 5000 0s and 5000 1s
    carlo = ([0] * 5000) + ([1] * 5000)
    # we will now use the random shuffle method on the array
    random.shuffle(carlo)
    return carlo

'''
In this function we will actually implement the Monte Carlo algorithm.
We will randomly search through an inputted array, which will be constrained
by an inputted number of attempts (k) until a 1 is found or was not found
in that many attempts. We will then return the index of where the first 1 is
found and how many tries it took before finding the 1 (or giving up after k attempts).
'''
def monteCarloAlg(A,k):
    # count for the tries it takes
    tries = 0
    # boolean to use so we can break out after a 1 is found
    found = False
    while tries < k and not found:
        # now to pick a random spot of the array
        position = random.randint(0, len(A) - 1)
        # checking if we found a 1 / need to break out
        if A[position] == 1:
            tries += 1
            found = True
            # letting the user know where a 1 was found and how many tries it took
            print(f"A '1' was found at position {position} of the array after {tries} tries.")
        # if we did not find a 1 just increase count of tries
        else:
            tries += 1

    # letting user know if a 1 was not found
    if not found:
        print(f"A '1' was not found after {k} tries.")

'''
This is our main function where we will implement the above functions
and test out the Monte Carlo algorithm on the randomized array of 0s and 1s.
We will output the position of the first 1 found as well as the number of tries.
If a 1 was not found in k tries we will also let the user know that.
'''
def main():
    k = 10
    # creating an array of 5000 0s and 5000 1s then randomly shuffling it
    a = randArray()
    # implementing randomized Monte Carlo algorithm on created array
    output = monteCarloAlg(a,k)


if __name__ == "__main__":
    main()
