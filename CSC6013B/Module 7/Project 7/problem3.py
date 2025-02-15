
def gcd(a, b):
    # Input: Two integers whose GCD is being determined
    # Output: Calculated value of the GCD of the two numbers that were passed in

    # the if and else statements below follow Euclid's algorithm that was given
    if b == 0:
        return a
    else:
        # to show the two integers being passed in before recursion
        print(f"Integers being passed in are: {a} and {b}")
        return gcd(b, a % b)

a = 2468
b = 1357
print(f"The GCD of {a} and {b} is:", gcd(a, b), "\n")

c = 111
d = 378
print(f"The GCD of {c} and {d} is:", gcd(c, d), "\n")

e = 123456789
f = 987654321
print(f"The GCD of {e} and {f} is:", gcd(e, f))
