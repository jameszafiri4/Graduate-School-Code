
def mean(A, n):
    # Input: An array of numbers and an integer that specifies how many numbers to include in calculation
    # Output: The calculated mean of numbers in an array that was given

    # base case; if n is 1 then it returns the one number that's in the array
    if n == 1:
        return A[0]
    # calculation based off of example using recursion to return the mean
    else:
        return (((n-1) / n) * mean(A, n-1)) + ((1/n) * A[n-1])

A1 = [12, 23, 37, 45, 63, 82, 47, 75, 91, 88, 102]

A2 = [-1.7, 6.5, 8.2, 0.0, 4.7, 6.3, 9.5, 12.2, 37.9, 53.2]

print(mean(A1, 11))
print(mean(A2, 10))
