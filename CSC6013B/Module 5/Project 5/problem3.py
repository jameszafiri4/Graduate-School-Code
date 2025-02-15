
def power(x, p):
    # to handle if the power is a zero
    if p == 0:
        return 1
    
    num = x
    # loops through each number to the specified power
    for i in range(1, p):
        # keeps multiplying itself by that number then returns when done
        num *= x
    return num

def evaluate(A, x):
    n = 0
    # loops through each item of the array, returns added total when done
    for i in range(len(A)):
        # uses index of item to call power function using that value
        n += A[i] * power(x, i)
    return n

A = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]

x = 5.4

print(evaluate(A, x))
