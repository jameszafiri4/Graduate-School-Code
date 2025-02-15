# this program uses a rectangle class as well as a child parallelepiped class and obtains length, width, and height inputs from the user
# the program then displays the perimeter and area of a rectangle, as well as the volume of a parallelepiped using the classes

# this is a class representing a rectangle
class Rectangle:
    # takes in a length and width as parameters for the constructor
    def __init__(self, l, w):
        self.length = l
        self.width = w
    # creates a method to calculate the perimeter
    def Perimeter(self):
        return 2 * (self.length + self.width)
    # creates a method to calculate the area
    def Area(self):
        return self.length * self.width
    # creates a method to display the values using an instantiation of the rectangle class
    def display(self):
        print("The length of the rectangle is:", self.length)
        print("The width of the rectangle is:", self.width)
        print("The perimeter of the rectangle is:", self.Perimeter())
        print("The area of the rectangle is:", self.Area())

# this is a child class that inherits the parent class Rectangle
class Parallelepiped(Rectangle):
    # takes in height in addition to the length and width as parameters
    def __init__(self, l, w, h):
        # calls the constructor method from parent class
        Rectangle.__init__(self, l, w)
        # creates new object for the height
        self.height = h
    # creates a method to calculate the volume
    def Volume(self):
        return (self.length * self.width) * self.height

# main function to ask for inputs and display values
def main():
    try:
        # asks for two inputs from the user and stores them as variables; absolute value incase input is negative
        x = abs(float(input("Please enter a length for the rectangle: ")))
        y = abs(float(input("Please enter a width for the rectangle: ")))
        # print new line to seperate from inputs
        print(" ")
        
        # takes the user's inputs and enters them into the Rectangle class     
        user_Rectangle = Rectangle(x, y)
        # calls the display function from the class and prints values for user
        user_Rectangle.display()
        # print new line to seperate from parallelepiped
        print(" ")
        
        # asks user for a height; absolute value incase input is negative
        z = abs(float(input("Please enter a height for the parallelepiped: ")))
        # takes user's input for height and enters into parallelepiped class
        user_Parallelepiped = Parallelepiped(x, y, z)
        # prints the volume of the parallelepiped using the called function from the class
        print("The volume of the parallelepiped is:", user_Parallelepiped.Volume())
        # exception handling to make sure user inputs valid numbers for length width and height
    except ValueError:
        print("\nPlease run the program again and enter a valid number.")
            
# calls main function
if __name__ == "__main__":
    main()
