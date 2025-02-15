from battleship import isGameOver, setupBoard, hitOrMiss
import unittest

# using the python module unit test class to test the program
class TestShip(unittest.TestCase):
    def testGameOverFalse(self):
        # sets up the grid
        grid_size = 10
        grid = [[""] * grid_size for i in range(grid_size)]
        # calling setupBoard to set up the ships on the board
        myBoard = setupBoard(grid)
        # the board has ships left; the game is not over
        self.assertEqual(isGameOver(myBoard), False)

    def testGameOverTrue(self):
        # sets up the grid
        grid_size = 10
        grid = [[""] * grid_size for i in range(grid_size)]
        # the board has no ships left; the game is over
        self.assertEqual(isGameOver(grid), True)

    def testShipCount(self):
        # starting variable for ship count
        shipCount = 0
        # sets up grid
        grid_size = 10
        grid = [[""] * grid_size for i in range(grid_size)]
        # calling setupBoard to set up the ships on the board
        myBoard = setupBoard(grid)

        # this loops over the game board
        for i in range(grid_size):
            for j in range(grid_size):
                # adds a ship to the count when it sees a ship; "S"
                if myBoard[i][j] == " S ":
                    shipCount += 1
        # this makes sure there are 5 ships
        self.assertEqual(shipCount, 5)

    def testShipCountBlank(self):
        # starting variable for blank spots
        blankCount = 0
        # sets up grid
        grid_size = 10
        grid = [[""] * grid_size for i in range(grid_size)]
        # calling setupBoard to set up the ships on the board
        myBoard = setupBoard(grid)

        # loops over the game board
        for i in range(grid_size):
            for j in range(grid_size):
                # adds a blank spot to the count when it sees a " . "
                if myBoard[i][j] == " . ":
                    blankCount += 1
        # makes sure the rest of the spots on the board are blank (95/100)            
        self.assertEqual(blankCount, 95)

    def testHit(self):
        # sets up grid
        grid_size = 10
        grid = [[""] * grid_size for i in range(grid_size)]
        # calling setupBoard to set up ships on the board
        myBoard = setupBoard(grid)
        # setting a ship to 0,0 so that the test can work everytime there is an "S"
        myBoard[0][0] = " S "
        # checks to see if there is a ship at 0,0 - whatever value is entered
        shot = hitOrMiss(myBoard, 0, 0)
        # checks to see if hit is returned by the function
        self.assertEqual(shot, "HIT")

    def testMiss(self):
        # sets up grid
        grid_size = 10
        grid = [[""] * grid_size for i in range(grid_size)]
        # calling setupBoard to set up ships on the board
        myBoard = setupBoard(grid)
        # setting a blank to 0,0 so that the test can work anytime no matter where the ships are
        myBoard[0][0] = " . "
        # checks to see if there is a blank spot at 0,0 - whatever value is entered
        shot = hitOrMiss(myBoard, 0, 0)
        # checks to see if miss is returned by the function
        self.assertEqual(shot, "MISS")


if __name__ == "__main__":
    unittest.main()
