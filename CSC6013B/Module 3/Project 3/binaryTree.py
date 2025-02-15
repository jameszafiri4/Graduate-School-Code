'''
This file contains the classes for a node as well as a binary tree
The binary tree class will be able to insert node correctly based
off what the nodes are to the left and the right, and will know what
to do if there is no value there. The class will also create a matrix
and will be able to print that matrix out by looping through the tree
and accounting for each row of the matrix
'''

class Node:
    def __init__(self, d):
        self.Data = d
        self.Left = None
        self.Right = None


class BinaryTree:
    def __init__(self, data, d = None):
        self.loop = 0 # when creating matrix this will count through each loop of tree
        self.data = data # to know where to insert nodes into matrix
        if (d == None): # an empty tree
            self.Root = None
        else:
            self.Root = Node(d)

    def insert(self, d):
        def __insertHere__(n, d):
            if (n.Data > d): # if no node left insert here
                if (n.Left == None):
                    n.Left = Node(d)
                else: # or try left child
                    __insertHere__(n.Left, d)
            elif (n.Data < d): # if no node right insert here
                if (n.Right == None):
                    n.Right = Node(d)
                else: # or try right child
                    __insertHere__(n.Right, d)
        
        if (self.Root == None): # it was an empty tree
            self.Root = Node(d)
        else:
            if (self.Root.Data > d): # try left child
                if (self.Root.Left == None): # if empty insert here
                    self.Root.Left = Node(d)
                else: # try left subtree
                    __insertHere__(self.Root.Left, d)
            elif (self.Root.Data < d): # try right child
                if (self.Root.Right == None): # if empty insert here
                    self.Root.Right = Node(d)
                else: # try right subtree
                    __insertHere__(self.Root.Right, d)

    def check(self, d):
        def __check__(n, d):
            if (n == None):
                return False
            elif (n.Data == d):
                return True
            elif (n.Data > d):
                return __check__(n.Left, d)
            elif (n.Data < d):
                return __check__(n.Right, d)
        return __check__(self.Root, d)

    def printInorder(self):
        def __visit__(n):
            if (n != None):
                __visit__(n.Left)
                print(n.Data, end = " ")
                __visit__(n.Right)
        print("\n--------")
        __visit__(self.Root)
        print("\n--------")

    def printPreorder(self):
        def __visit__(n, h):
            if (n != None):
                print("---" * h, n.Data)
                __visit__(n.Left, h + 1)
                __visit__(n.Right, h + 1)
        print("^^^^^^^^^^")
        __visit__(self.Root, 1)
        print("^^^^^^^^^^")

    def printPostorder(self):
        def __visit__(n, h):
            if (n != None):
                __visit__(n.Left, h + 1)
                __visit__(n.Right, h + 1)
                print("---" * h, n.Data)
        print("==========")
        __visit__(self.Root, 1)
        print("==========")

    
    def buildMatrix(self, num):
        '''
        This method will create the adjacent matrix that we want
        based off of the number of items that are in Tree
        It will be a for loop within a for loop, so that it can create
        a matrix that is n x n
        '''
        matrix = [[0 for n in range(num)] for n1 in range(num)]
        return matrix
                
    def printMatrix(self):
        '''
        This method will print out the matrix by looking at
        the left and right of each node and then add it to the
        matrix we just created
        '''
        matrix = self.buildMatrix(len(self.data))

        def __visit__(n, matrix):
            if (n != None): # if there is no node
                if (n.Left != None or n.Right != None): # if there is a node to left/right
                    node = n.Data
                    data = self.data
                    # we are first going to try the left
                    try:
                        left = n.Left.Data # node to the left of current node
                        leftValue = abs(node - left) # what the left node weight is
                        newLeft = data.index(int(left)) # where to enter in matrix
                        
                        # updating the matrix row which is based off of the loop through the tree
                        matrix[self.loop][newLeft] = leftValue        
                    except:
                        # if there is nothing to the left
                        pass
                    # now we are going to try the right
                    try:
                        right = n.Right.Data # node to the right of current node
                        rightValue = abs(node - right) # what the right node weight is
                        newRight = data.index(int(right)) # where to enter in matrix
                        
                        # updating the matrix row which is based off of the loop through the tree
                        matrix[self.loop][newRight] = rightValue
                    except:
                        # if there is nothing to the right
                        pass
                    # to count that we looped through a row
                    self.loop += 1
                else:
                    # tries next row if there was nothing to left/right
                    self.loop += 1
                # recursion with both the left and right sides
                __visit__(n.Left, matrix)
                __visit__(n.Right, matrix)
                
        print("\n------------------")
        # starting at the root of the tree
        __visit__(self.Root, matrix)
        # prints out each row of the matrix
        for row in matrix:
            print(row, ",")
        print("------------------")


