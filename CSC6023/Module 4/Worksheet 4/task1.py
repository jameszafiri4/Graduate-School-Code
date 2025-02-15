'''
In this program we will run the Egyptian Fractions for the
following examples:

5/6, 7/15, 23/34, 121/321, 5/123

The comments will show the correct results for each example.
'''

from math import ceil
  
# n is the numerator, d is the denominator
def egyptian(n, d):
  
    print("\nThe Egyptian Fraction of {}/{}".format(n, d))
    ans = []
    # while numerator is not 0
    while (n > 0):
        x = ceil(d / n)          # compute the minimal larger denominator
        ans.append(x)            # hold it to the denominator list
        n, d = x * n - d, d * x  # update the remainder to n and d
    for a in ans:
        print("1/{}".format(a), end=" ")

# we will look at the results in the main function
def main():
    # the solution is: 1/2 + 1/3
    ex_one = egyptian(5,6)
    # the solution is: 1/3 + 1/8 + 1/120
    ex_two = egyptian(7,15)
    # the solution is: 1/2 + 1/6 + 1/102
    ex_three = egyptian(23,34)
    # the solution is: 1/3 + 1/23 + 1/7383
    ex_four = egyptian(121,321)
    # the solution is: 1/25 + 1/1538 + 1/4729350
    ex_five = egyptian(5,123)


if __name__ == "__main__":
    main()
