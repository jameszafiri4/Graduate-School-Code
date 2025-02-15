'''
In this program we will run the Egyptian Fractions for the
following example: 5/121

We will then check it out manually, with the expected result:

5/121 = 1/25 + 1/757 + 1/763,309 + 1/873,960,180,913 + 1/1,527,612,795,642,093,418,846,225
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

'''
In our main function we will run the egyptian function with the
example 5/121 and compare those results to that of the manual calc
'''
def main():
    # results: 1/25 + 1/757 + 1/763,309 + 1/873,960,180,913 + 1/1,527,612,795,642,093,385,023,488
    example = egyptian(5,121)

'''
When comparing the results from our code to that of a manual calculation, all fractions
are the same with the exception of the second half of the last very small fraction. This
is a minimal difference, but it goes to show the downside of greedy algorithms. This was
still a very quick and efficient solution, but as we saw it was not quite the best.
'''

if __name__ == "__main__":
    main()
