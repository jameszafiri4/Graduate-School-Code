'''
In this assignment we will create a program that receives the list of possible
named items with the following info: Value($), Height(in), Width(in), Depth(in)

The limit of the optimal solution is expressed by the volume in cubic inches (in3)
and the program will maximize the value within the cubic limit. We will read a
textual file that has one item per line with the information separated by commas

The program will capture the overall limit of the package/knapsack from the user
and it will be able to read any file that has the info mentioned above per line.

We will then print out the best possible distribution to the user, which will
include all the needed information of the items
'''

# we will first import the knapsack function given to us so we can use that
from KnapSack import knapsack
# we are also importing the csv module so we can read the file
import csv


'''
We will now implement our main function where we will do all of the work needed
to read the file and give the user the best possible distribution based on their input.
'''
def main():
    # we will first need a variable to read the file
    file = open("packs.csv", "r")
    # now using the module to create an array based on the file
    read = csv.reader(file)
    # exception handling to capture valid input
    try:
        # we will now create a variable for the volume limit of the items based on user input
        volume = int(input("Please enter a limit for the volume of the knapsack: "))
        # making sure user gives a valid number for the limit
        if volume < 0:
            print("Please run again and give a valid volume limit.")
        else:
            # we will also create an empty array to store the items from the file
            sack = []

            # it is now time to read through the file and add values to the array
            for i in read:
                # adding values to the array based on what it represents
                name = i[0]
                value = int(i[1])
                height = int(i[2])
                width = int(i[3])
                depth = int(i[4])
                # now creating variable for volume of the item
                vol = height * width * depth
                # adding items info to the list we created
                sack.append((name, value, vol))

            # we will now implement the knapsack algorithm to select which items to include
            solution = knapsack([i[1] for i in sack], [i[2] for i in sack], volume)
            # now we will make a new list of the items that were just chosen
            items = [sack[i] for i in solution]
            # variable that gives you the name of the selected items
            names = [i[0] for i in items]
            # variable that tells you the total value of the items
            total_val = sum([i[1] for i in items])
            # variable that tells you the total volume of the items
            total_vol = sum([i[2] for i in items])
            # variable to account for leftover space
            leftover = volume - total_vol

            # we will now print it all out
            # names of the items, total number of items, total value, total volume, and the leftover volume
            print("\nHere are the suggested items:\n")
            print(f"Names of items: {names}\n\nTotal items: {len(items)}\nTotal value: {total_val}\nTotal volume: {total_vol}\nLeftover space: {leftover}")
    # in case user enters a non-integer character
    except ValueError:
        print("Please run again and enter a valid integer for the volume limit.")


if __name__ == "__main__":
    main()
