'''
Find the number of entries in an array of integers that are divisible by a given integer.
Your function should have two input parameters – an array of integers and a positive integer.
It should return an integer indicating the count using a return statement.

Run your algorithm on the problem instances:
a) [20, 21, 25, 28, 33, 34, 35, 36, 41, 42] number of entries that are divisible by 7
and
b) [18, 54, 76, 81, 36, 48, 99] number of entries that are divisible by 9

'''

def divisible(a, n):
    '''
    This function takes two inputs; an array and an integer
    It will start the count at zero and add a number from
    the array to the count if that number is divisible by the inputted int
    '''
    count = 0
    for num in a:
        if num % n == 0:
            count += 1

    return count

a1 = [20, 21, 25, 28, 33, 34, 35, 36, 41, 42]
n1 = 7

a2 = [18, 54, 76, 81, 36, 48, 99]
n2 = 9

print(divisible(a1, n1))
print(divisible(a2, n2))
