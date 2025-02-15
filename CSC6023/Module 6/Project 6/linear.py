'''
In this program we will implement a Linear Programming solver

The program will receive the necessary information for an LP problem namely:

○The number of variables (equal to the number of constraint coefficients)

■ x

○The coefficient of each variable for the objective function

■ f(x)

○The data for the square matrix stating the constraint

■ A

○The constraint limits

■ b


Having all input parameters, we will compute the possible solution for each
variable alone and the solution of the linear equation system Ax = b


○To solve the linear equation system we will use the numpy package

■ We will import numpy and use the functions:

array(...) to create a numpy array
linalg.inv(...) to perform a matrix inversion
linalg.dot(...) to perform a dot product


○For example, the input can be:

○3 variables/constraints, [3,2,2] as weights for the objective function
A = [[2,4,5],[1,2,4],[8,0,3]], and b = [300,200,300]

The output will be the Real number of unit to each of the variables
'''

# we will first import the numpy module
import numpy as np

'''
In this function we will implement the solving of the linear
program. We will communicate with the user and create arrays
based on their inputs for constraints/variables/coefficients.
'''
def main():
    # loop to handle working with user inputs
    while True:
        # exception handling so program does not crash
        try:
            # getting variable number
            x = int(input("Please enter the number of variables: "))
            # need at least one variable, will let user know
            if x < 1:
                print("\nPlease enter at least one variable.\n")
            else:
                # array of coefficients for objective function (profits)
                fx = []
                print("\nPlease enter the profit for each variable (click enter after each): ")
                # receiving user input for each by looping and adding based on # of variables
                for i in range(0, x):
                    coeff = float(input())
                    fx.append(coeff)

                # array of constraint limits
                b = []
                print("\nPlease enter the constraint limits for each variable (click enter after each): ")
                # receiving user input for each by looping and adding based on # of variables
                for i in range(0, x):
                    limit = float(input())
                    b.append(limit)

                # square matrix for constraint data
                A = []
                print("\nPlease enter the square matrix data as constraint for each variable (enter after each): ")
                # receiving user input for each by looping and adding based on # of variables
                for i in range(x):
                    a = []
                    # nested for loop to create the matrix (square based on # of variables)
                    for j in range(x):
                        a.append(float(input()))
                    A.append(a)

                # implementation seen in class to calculate the balanced array
                A = np.array(A)
                b = np.array(b)
                balanced_array = np.linalg.inv(A).dot(b)

                # now we will calculate the solo options
                # making copy of constraint limit arrays
                lowest_results = b.copy()
                # looping through based off variable size
                for i in range(x):
                    # nested loop to work with square matrix
                    for j in range(x):
                        # lowest division being kept track of
                        lowest = float((b[i])/(A[i][j]))
                        # comparing lowest calc to what is already in results array
                        if (lowest < lowest_results[j]):
                            lowest_results[j] = lowest
                            
                # empty list for profit calcs
                products = []
                # loop through based on variable size to find products
                for i in range(x):
                    product = lowest_results[i] * fx[i]
                    products.append(product)

                # printing out the table for the user to see what we're working with
                print("\nSupplies:\n",A)
                print("\nAvailability:\n",b)
                print("\nProfit (per row):", fx)
                print("")
                # printing out the profit for each solo option
                for i in range(len(products)):
                    print(f"The total amount for only '{i}' is: {products[i]}")
                # showing what the balanced array is using
                print("\nThe breakdown of the balanced amount is:", balanced_array)
                # to get dollar amount
                balanced_sol = np.dot(balanced_array, fx)
                print("The total balanced amount is:", balanced_sol)

                # loop to find the best solution of all profit options
                highest = balanced_sol
                for i in range(len(products)):
                    if products[i] > highest:
                        highest = products[i]
                print("\nThe best solution for the most profit is:", highest)
                break

        except ValueError:
            print("\nPlease enter a valid integer.\n")

            
if __name__ == "__main__":
    main()


# below shows to code being ran using pants & jackets example - how the user should interact

'''
Please enter the number of variables: 2

Please enter the profit for each variable (click enter after each): 
50
40

Please enter the constraint limits for each variable (click enter after each): 
1500
1000

Please enter the square matrix data as constraint for each variable (enter after each): 
2
3
2
1

Supplies:
 [[2. 3.]
 [2. 1.]]

Availability:
 [1500. 1000.]

Profit (per row): [50.0, 40.0]

The total amount for only '0' is: 25000.0
The total amount for only '1' is: 20000.0

The breakdown of the balanced amount is: [375. 250.]
The total balanced amount is: 28750.0

The best solution for the most profit is: 28750.0
'''
