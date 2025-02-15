'''
In this program we will create a recursive function that will deliver the
minimal number of moves needed to solve the Towers of Hanoi efficiently
when the user is asked to enter a number of disks. I will know my program
is correct by matching it up with the Tower of Hanoi game link that we
were given in class. There I will see if the numbers of moves my program
outputs is correct.
'''

'''
This function is using recursion to find the minimum number of moves (output)
needed to solve for given number of disks(input).
'''
def tower_of_hanoi(n):
    # this will be our base case; if there is one disk
    if n == 1:
        return 1
    # if not we will use a recursive formula based on the example seen in class
    else:
        return 2 * tower_of_hanoi(n-1) + 1

    
'''
This is our main function where we ask the user to enter a number
of disks and then call the recursive function above to print out
the minimum number of moves needed for specific Tower of Hanoi problem.
'''
def main():
    # exception handling incase a user enters an invalid input
    try:
        disks = int(input("Please enter the number of disks: "))
        # if user enters 0 or negative number
        if disks < 1:
            print("\nThere has to be at least 1 disk in the game. Run it again.")
        # if valid number is entered, call recursive function
        else:
            moves = tower_of_hanoi(disks)
            print(f"\nThe minimum number of moves needed is {moves}.")
    # if user enters a letter/symbol
    except ValueError:
        print("\nPlease enter a valid number. Run program again.")

if __name__ == "__main__":
    main()
