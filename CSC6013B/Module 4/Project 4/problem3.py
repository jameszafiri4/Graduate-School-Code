'''
Given an integer n>=2 and two nxn matrices A and B of real numbers, find the product AB of the matrices.
Your function should have three input parameters – a positive integer n and two nxn matrices of numbers
The function should return the nxn product matrix using a return statement.
'''

def matrix_multiply(n, x, y):
    '''
    This function will take an integer and two matricies as inputs
    It will use nested loops to go through each matrix and
    multiply its values correspondingly
    '''
    # nested loop to create matrix
    m = [[0 for i in range(n)] for j in range(n)]

    # first looping through x's rows
    for i in range(len(x)):
        # then looping through y's columns 
        for j in range(len(y[0])):
            # lastly looping through y's rows
            for k in range(len(y)):
                m[i][j] += x[i][k] * y[k][j]

    return m

n1 = 2
x1 = [[2, 7], [3, 5]]
y1 = [[8, -4], [6, 6]]

n2 = 3
x2 = [[1, 0, 2], [3, -2, 5], [6, 2, -3]]
y2 = [[0.3, 0.25, 0.1], [0.4, 0.8, 0], [-0.5, 0.75, 0.6]]

print(matrix_multiply(n1, x1, y1))
print(matrix_multiply(n2, x2, y2))
