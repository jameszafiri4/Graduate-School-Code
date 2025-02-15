from Project04 import Rectangle, Parallelepiped
import unittest

# using python module unit test class
class TestCalculations(unittest.TestCase):
    # this will test the perimeter method from Rectangle class
    def testPerimeter(self):
        # two variables to test the calc; one with a decimal
        perimeter = Rectangle(4, 5).Perimeter()
        decPerimeter = Rectangle(3.25, 6.75).Perimeter()
        # checking if equal to value using given parameters
        self.assertEqual(perimeter, 18)
        self.assertEqual(decPerimeter, 20)
    # this will test the area method from Rectangle class
    def testArea(self):
        # two variables to test the calc; one with a decimal
        area = Rectangle(7, 9).Area()
        decArea = Rectangle(5.5, 8.5).Area()
        # checking if equal to value using given parameters
        self.assertEqual(area, 63)
        self.assertEqual(decArea, 46.75)
    # this will test the volume method from Parallelepiped class
    def testVolume(self):
        # two variables to test the calc; one with a decimal
        volume = Parallelepiped(2, 5, 9).Volume()
        decVolume = Parallelepiped(3.5, 7.5, 8.5).Volume()
        # checking if equal to value using given parameters
        self.assertEqual(volume, 90)
        self.assertEqual(decVolume, 223.125)

if __name__ == "__main__":
    unittest.main()
