'''
Given an array of real numbers, without sorting the array, find the smallest gap between all pairs of elements.
(For an array A, the absolute value of the difference between elements 𝐴[i] and 𝐴[𝑗]).
Your function should have one input parameter – an array of numbers.
It should return a non-negative number indicating the smallest gap using a return statement.

Run your algorithm on the problem instances:
a) <50, 120, 250, 100, 20, 300, 200>
b) <12.4, 45.9, 8.1, 79.8, -13.64, 5.09>

'''

def smallestGap(a):
    '''
    This function takes an array as an input
    It will use nested loops to look at the
    elements in pairs, and find the smallest
    gap between them
    '''
    # infinite number as placeholder to compare gaps
    small_gap = float("inf")
    num = len(a)
    # loop through array
    for i in range(num):
        # second loop to compare next element
        for j in range(i + 1, num):
            # gap between the pair
            gap = abs(a[i] - a[j])
            # sets initial gap to new value and loops again
            if gap < small_gap:
                small_gap = gap

    return small_gap

a1 = [50, 120, 250, 100, 20, 300, 200]

a2 = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]

print(smallestGap(a1))
print(smallestGap(a2))
