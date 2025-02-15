
# will import math module to use the floor function
import math

def digits(n):
    # Input: A positive integer "n"
    # Output: Returns number of digits in the binary representation of n

    # base case to return 1
    if n == 1:
        return 1
    # 1 more than number of digits in binary representation
    else:
        return 1 + digits(math.floor(n/2))

print(digits(256))

print(digits(750))
