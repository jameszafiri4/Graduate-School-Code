
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
        # creating 1000 random ints between 1 and 1 mill (inclusive)
        n = random.randint(1, 1000001)
        # adding random number to vector we created
        myVector.append(n)
    # this returns the fully complete vector after loop
    return myVector

'''
This function below will determine the uniqueness (output) of the elements of
an array (input) by using a brute force algorithm that is in O(n^2)
'''
def uniqueBrute(a):
    # set uniqueness to True to start
    ans = True
    # loop through entire array
    for i in range(len(a)):
        # nested loop to compare elements of array
        for j in range(len(a)):
            # checking to see if two elements are the same
            if (i != j) and (a[i] == a[j]):
                # if condition applies then it is not unique
                ans = False
                break
        # otherwise after iterating above
        if (not ans):
            break
    return ans

'''
This function below will determine the uniqueness (output) of the elements of
an array (input) by using a more efficient transform-and-conquer algorithm
that is in O(n*log(n))
'''
def uniqueTransform(a):
    # first sorting the array
    a.sort()
    # loop to iterate through sorted array
    for i in range(len(a)):
        # checking if elements next to each other are the same
        if (a[i-1] == a[i]):
            return False
    # after iterating above and nothing found, it is unique
    return True

'''
In our main function we will create a random array and test out
both of the uniqueness algorithms, and print the resut (output)
'''
def main():
    # creating random array
    A = randomVector()
    # now we try the brute function and print our results
    brute = uniqueBrute(A)
    print("By first using the brute force algorithm...")
    print("The array is unique:", brute)
    # next we try the transform function and print our results
    transform = uniqueTransform(A)
    print("\nNow using the transform-and-conquer algorithm...")
    print("The array is unique:", transform)    


if __name__ == "__main__":
    main()

