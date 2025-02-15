'''
In this program we will run the balanced01mat.py program that we were given
in class. We will keep everything the same, but just change it so that instead
of asking the user for a number input, we will call it for values of 2,4,6
(8 will take very long to run; not being included). I will include comments
above each of the calls to give my expected values.
'''

from itertools import combinations

def permutations(n):
    ones = list(combinations(list(range(n)),n//2))
    ans = []
    for o in ones:
        case = []
        for i in range(n):
            if (i in o):
                case.append(1)
            else:
                case.append(0)
        ans.append(case)
    return ans

def check(mat):
    n = len(mat[0])
    for j in range(n):
        acc0, acc1 = 0, 0
        for i in range(len(mat)):
            if (mat[i][j] == 1):
                acc1 += 1
            elif (mat[i][j] == 0):
                acc0 += 1
            if (acc0 > (n//2)) or (acc1 > n//2):
                return False
    return True

def layer(r, mat, perm, ans):
    for p in perm:
        mat.append(p)
        if check(mat):
            if (r+1 == len(p)):
                ans += 1
            else:
                ans = layer(r+1, mat, perm, ans)
        mat.pop()
    return ans

def balanced01mat(n):
    print("\nComputing the number of balanced matrices...")
    print(f"Using size of {n}...")
    perm = permutations(n)
    ans = layer(0, [], perm, 0)
    print("\nThe number of balanced matrices is", ans)

'''
This is our main function where we will call the balanced01mat
function for each of the values we want to test. I expect them
to grow exponentially, thinking about how when you keep squaring
a number, the next one will get a lot bigger each time.
'''
def main():
    a = 2
    b = 4
    c = 6

    # with a 2 by 2 matrix, I would expect the output to be 2
    # this is because to be balanced you can only change it once
    balanced01mat(a)
    # with a 4 by 4 matrix, I would expect the output to be around 64
    # to get this I guessed by squaring 4, and then multiplying by 4
    balanced01mat(b)
    # with a 6 by 6 matrix, I would expect the output to grow to around 50k
    # to get this I guessed by squaring 6, multiplying by 6, then squaring that
    balanced01mat(c)

if __name__ == "__main__":
    main()

