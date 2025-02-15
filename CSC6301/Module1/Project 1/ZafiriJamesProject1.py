''' James Zafiri 08/31/2023
    This module holds the class of a rectangle and is able to obtain length
    and width values. It will be able to calculate the perimeter and area
    of a rectangle and display these to the user. '''

class Rectangle:
    ''' This class defines a rectangle and it has 2 instance variables:
        - length variable
        - width variable
        These will be used to make calculations for the rectangle. '''
    def __init__(self, l, w):
        ''' The constructor of a rectangle that takes in a length and
            width for the rectangle as parameters and assigns them. '''
        self.length = l
        self.width = w
    def Perimeter(self):
        ''' This method is meant to calculate the perimeter of a rectangle
            using the values given from length and width. '''
        return 2 * (self.length + self.width)
    def Area(self):
        ''' This method is meant to calculate the area of a rectangle
            using the values given from length and width. '''
        return self.length * self.width
    def display(self):
        ''' This method is meant to display and print out the values
            of the rectangle using an instantiation of the class. '''
        print("The length of the rectangle is:", self.length)
        print("The width of the rectangle is:", self.width)
        print("The perimeter of the rectangle is:", self.Perimeter())
        print("The area of the rectangle is:", self.Area())

