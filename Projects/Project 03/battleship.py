"""
    ----------------------BATTLESHIP----------------------
    How it will work:
    1. A 10x10 grid will have 5 ships randomly placed about
    2. You can choose a row and column to indicate where to shoot
    3. For every shot that hits or misses it will show up in the grid
    4. If all ships are shot, game over

    Legend:
    1. "." = water
    2. "S" = ship position
    3. "O" = water that was shot with bullet, a miss because it hit no ship
    4. "X" = ship sunk!
"""

import random

# global variable for size of grid
grid_size = 10
# global variable for the grid
grid = [[""] * grid_size for i in range(grid_size)]
# global variable for number of ships
num_of_ships = 5

# this displays the game board (as a 2d array)
def drawBoard(myBoard):
    # prints the top row of the board
    board = '''
    +---+---+---+---+---+---+---+---+---+---+---+
    |   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
    +---+---+---+---+---+---+---+---+---+---+---+
    '''
    # this will go through and print each row of the board
    for i in range(grid_size):
        draw = f'''
    | {i} |{myBoard[ i ][0]}|{myBoard[ i ][1]}|{myBoard[ i ][2]}|{myBoard[ i ][3]}|{myBoard[ i ][4]}|{myBoard[ i ][5]}|{myBoard[ i ][6]}|{myBoard[ i ][7]}|{myBoard[ i ][8]}|{myBoard[ i ][9]}|
    +---+---+---+---+---+---+---+---+---+---+---+
    '''
        board = board + draw
    print(board)

# this sets up the game board (as a 2d array)
def setupBoard(myBoard):
    # first set everything on the board to .
    for i in range(grid_size):
        for j in range(grid_size):
            myBoard[i][j] = " . "
    # enter the ships now
    # use the randint to put the ships in random rows/columns based on the number of ships
    for i in range(0, num_of_ships):
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)
        # this will show the random ships as an S
        myBoard[randomRow][randomCol] = " S "
    # returning value of myBoard
    return myBoard

# this checks if user input is a hit or a miss on the board and updates it as well
def hitOrMiss(myBoard, row, col):
    # checks if the board has an S and replaces it to an X; lets you know it's a hit
    if myBoard[row][col] == " S ":
        myBoard[row][col] = " X "
        print("HIT")
        return "HIT"
    # checks if there is an X on the board and still tells you it's a hit
    elif myBoard[row][col] == " X ":
        print("HIT")
        return "HIT"
    # if there was no ship then it will place an O on the board and say you missed
    else:
        myBoard[row][col] = " O "
        print("MISS")
        return "MISS"
    return

# this is to check if the game is over or not so the program can keep looping
def isGameOver(myBoard):
    # make an empty list to hold booleans
    linestats = []
    # checks each row if it has an S and says false or true then adds to the list
    for i in range(grid_size):
        if " S " in myBoard[i]:
            linestats.append(False)
        else:
            linestats.append(True)
    # checks if false is in the list and returns False, otherwise returns True to show there are no S left on board       
    if False in linestats:
        return False
    else:
        return True

def main(myBoard):
    # sets up the board
    myBoard = setupBoard(myBoard)
    # displays the board
    drawBoard(myBoard)
    # loops as long as game is not over
    while not isGameOver(myBoard):
        try:
            # takes the user input and also makes sure it is a valid row/col number
            row = int(input("Enter a row: "))
            if (row < 0) or (row >= 10):
                print("Invalid row")
                raise ValueError
            col = int(input("Enter a column: "))
            if (col < 0) or (col >= 10):
                print("Invalid column")
                raise ValueError
            # checks if the input is a hit or miss and lets the user know
            hitOrMiss(myBoard, row, col)
            # displays the updated board showing the last try (X or O)
            drawBoard(myBoard)       
        # exception handling for if user enters wrong row/col
        except ValueError:
            print("Please enter a valid number.")
            continue
    # lets the user know game is over at the end of the program (hit all ships)    
    print("Game Over!")

if __name__ == "__main__":
    main(grid)
