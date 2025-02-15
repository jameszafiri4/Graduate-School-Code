# this program will ask the user to enter 2 positive numbers and will return the Boolean True if they evenly divide eachother
# the program will continue running until it is True, even if the user inputs wrong values (like letters or negative numbers)

def main():
    loop = False # set to False so that I can keep the while loop running until condition is met
    while loop == False:
            
        try: # so I can use exception handling if user enters a string
            print("See if two positive integers evenly divide each other!")
            num1 = float(input("Enter the first positive number: "))
            num2 = float(input("Enter the positive number you want to divide it by: "))
            print("\n")

            if (num1 <= 0) or (num2 <=0): # this makes sure that both numbers are positive; the program will keep running if negatives are entered
                loop = False
            elif ((num1 % num2) == 0) or ((num2 % num1) == 0): # this makes sure that either combination of numbers is evenly divisible
                loop = True
                break # ensures to break the loop if True
            else: # other False outcomes will keep the loop going
                loop = False

        except ValueError: # exception handling if user enters a string
            print("\n")
            print("You didn't enter a number\n")

    print(loop) # prints boolean after loop breaks
    return loop # returns boolean after loop breaks

# function getting called
main()
