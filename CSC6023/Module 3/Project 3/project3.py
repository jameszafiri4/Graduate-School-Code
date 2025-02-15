'''
In this program we are going to be able to compute the "Tribonacci" sequence.
This is a spin off of the Fibonacci sequqence so that a number is the sum of
its three previous ones instead of the two previous ones (1,1,1 are initial).
The program will continue to ask the user for a positive integer n, and will
deliver the nth element of the Tribonacci sequence. 1,1,1,3,5,9,17,31,57,...
'''

'''
This is the function where we will implement the Tribonacci sequence and
return the element in the sequence (output) based off the number given (input)
'''
def tribonacci(n):
    # setting the initial 3 values of the sequence to 1
    a, b, c = 1, 1, 1
    # if number is one of the initial 3, return 1
    if (n < 4):
        return 1
    # loop through 4th element to whatever number is given
    for i in range(3, n):
        # change first and second elements to ones following it
        # change third element to sum of the 3 before it
        a, b, c = b, c, a + b + c
    # gives the element of the number user entered
    return c

'''
This is our main function where we will ask the user to enter an integer
to find the element of that value in the Tribonacci sequence.
'''
def main():
    # loop so we can keep asking user for numbers
    while True:
        # exception handling so the program does not crash with an invalid input
        try:
            # asking user to enter a number to find that element
            n = int(input("Please enter a positive integer to find that element in the Tribonacci sequence (0 or negative to exit): "))
            # exit program if number is less than 1
            if n < 1:
                break
            # if 1 or more, use the tribonacci function we created and print the element for the user
            else:
                element = tribonacci(n)
                print(f"\nThe {n} element of the Tribonacci sequence is: {element}.")
                print("\n")
        # in case user enters something that is not an integer
        except ValueError:
            print("\nPlease enter a valid integer.\n")


if __name__ == "__main__":
    main()
