'''
                JAMES ZAFIRI    WORKSHEET 1    CSC6013

This program will swap elements in a created vector

- It will first ask the user to enter an even integer between 9 and 21
- It will then create a vector of that size (number user entered)
- Next, it will swap the first element with the second, third with fourth, etc.
- After the swaps are complete, the final vector will be printed out

'''

def vectorSwap():
    # loop using exception handling to make sure user enters a valid number
    while True:
        try:
            size = int(input("Please enter an even integer between 9 and 21: "))
            
            # makes sure user input meets criteria
            if size < 9 or size > 21 or (size % 2) != 0:
                print("Invalid input. Follow instructions and try again.\n")

            else:
                vector = list(range(size))
                # loops through created vector and for every two iterations, swaps elements
                for i in range(0, size - 1, 2):
                    vector[i], vector[i + 1] = vector[i + 1], vector[i]
                print(vector)
                break
            
        except ValueError:
            print("Please enter a valid integer.\n")

vectorSwap()
