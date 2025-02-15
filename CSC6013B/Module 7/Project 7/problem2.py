
# importing math module to use floor function
import math

def BinarySearch(A, start, end, k):
    # Input: An array in descending order, start & end positions, and key "k" to look for
    # Output: Index i such that A[i] = k or None if a match was not found

    # middle of the array
    m = math.floor((end + start) / 2)
    # return None if item is not found
    if start > end:
        return None
    # to print out the "middle" subscript of array
    print(m)

    # if middle is what we are looking for, return it
    if A[m] == k:
        return m
    # if middle is less than it, search again from beginning to one less index of that middle (left)
    elif A[m] < k:
        return BinarySearch(A, start, m-1, k)
    # search to the right, one more index of that middle to end of array
    else:
        return BinarySearch(A, m+1, end, k)

A = [100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18]

BinarySearch(A, 0, 14, 87)
print("")
BinarySearch(A, 0, 14, 48)
print("")
BinarySearch(A, 0, 14, 33)
print("")
BinarySearch(A, 0, 14, 10)
