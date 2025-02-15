
def square_sums(n):
    # Input: A positive integer "n"
    # Output: Returns the sum of squares of all the integers going down to 1 from n

    # base case to return 1
    if n == 1:
        return 1
    # added n^2 to sum of squares for each n going down to base case
    else:
        return square_sums(n-1) + n**2

print(square_sums(12))

print(square_sums(20))
